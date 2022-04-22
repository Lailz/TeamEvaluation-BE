from asyncore import read
from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from team_app.models import Project, Semester, Team


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        payload = RefreshToken.for_user(new_user)
        token = str(payload.access_token)
        validated_data["token"] = token
        return validated_data


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    token = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)

        except:
            raise serializers.ValidationError("This username doesn't exist!")

        if not user.check_password(password):
            raise serializers.ValidationError(
                "Username / Password combination is incorrect")
        payload = RefreshToken.for_user(user)
        token = str(payload.access_token)
        data["token"] = token
        return data


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "slug"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "slug", "teams"]


class SemesterListSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Semester
        fields = ["id", "name", "slug", "projects"]


class SemesterCreateSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Semester
        fields = ["id", "name", "slug", "projects"]

    def get_projects(self, obj):
        return []


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "slug", "weight", "semester"]
