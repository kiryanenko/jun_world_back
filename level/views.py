from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.serializers import UserSerializer
from level.serializers import AddLevelProgressSerializer


class AddLevelProgressView(generics.CreateAPIView):
    serializer_class = AddLevelProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(UserSerializer(instance=request.user).data, status=status.HTTP_200_OK)
