# DRF
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

# Models
from team_app.models import Semester
from django.contrib.auth.models import User

# Serializers
from .serializers import ProjectCreateSerializer, SemesterCreateSerializer, SemesterListSerializer, SigninSerializer, SignupSerializer


# TODO: Fix slugify in signup
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


class SemesterListCreateView(ListCreateAPIView):
    queryset = Semester.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kargs):
        return self.list(request, *args, **kargs)

    def post(self, request, *args, **kargs):
        return self.create(request, *args, **kargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SemesterCreateSerializer
        return SemesterListSerializer

    # def perform_authentication(self, request):
    #     if self.request.method == 'POST':


class ProjectCreateView(CreateAPIView):
    serializer_class = ProjectCreateSerializer

    def perform_create(self, serializer):
        serializer.save(semester_id=self.kwargs["semester_id"])
