from dataclasses import fields
from pyexpat import model
from re import S
from rest_framework import serializers
from .models import User,Submissions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SubmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Submissions
        fields= "__all__"
