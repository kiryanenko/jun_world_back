from django.contrib.auth import login
# Create your views here.
from rest_framework import generics

from core.serializers import UserSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
