from winreg import QueryInfoKey
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from .models import User, Submissions
from .serializers import SubmissionsSerializer,UserSerializer
from .utils import create_code_file, execute_file
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import api_view, permission_classes

def hello_world(request):
    return HttpResponse("Welcome to online ide")


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

@api_view(http_method_names=["POST"])
@permission_classes((permissions.AllowAny,))
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(UserSerializer(user).data, status=201)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,) 
    queryset = User.objects.all()

    def list(self, request,*args, **kwargs):
       return Response(UserSerializer(request.user).data, status=200) 




class SubmissionsViewSet(ModelViewSet):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionsSerializer

    def create(self, request, *args, **kwargs):
        request.data["status"] = "P"
        file_name = create_code_file(request.data.get("code"),
                                     request.data.get("language"))
        output = execute_file(file_name, request.data.get("language"))
        request.data["output"] = output
        return super().create(request, args, kwargs)