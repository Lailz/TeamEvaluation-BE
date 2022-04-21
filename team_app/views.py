from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from team_app.models import Semester
from .serializers import SemesterCreateSerializer, SemesterListSerializer, SigninSerializer, SignupSerializer
from team_app import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

# Create your views here.

# TODO: Fix slugify in signup
# TODO: Move token generation to views


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer


class SigninView(APIView):
    serializer_class = SigninSerializer

    def post(self, request):
        data = request.data
        serializer = SigninSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)


class SemesterListView(ListAPIView):
    queryset = Semester.objects.all().order_by("-created_at")
    # .order_by("")
    serializer_class = SemesterListSerializer


class SemesterCreateView(CreateAPIView):
    serializer_class = SemesterCreateSerializer
