from urllib.parse import urlparse
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("user", views.UserViewSet) 
router.register("submit" , views.SubmissionsViewSet)

urlpatterns = [

]

urlpatterns += router.urls