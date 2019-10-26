from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from achievement.models import Achievement
from core.serializers import UserSerializer


class GetAchievementView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, slug='', **kwargs):
        achievement = get_object_or_404(Achievement, slug=slug)
        achievement.users.add(request.user)
        request.user.rating += achievement.points
        request.user.save()
        return Response(UserSerializer(instance=request.user).data, status=status.HTTP_200_OK)
