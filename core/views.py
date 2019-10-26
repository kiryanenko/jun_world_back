from django.contrib.auth import login
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from core.serializers import UserSerializer, SignInSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)


class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
