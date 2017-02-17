from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class PingView(views.APIView):

    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        return Response(dict(ping="PONG, BRUH"), status.HTTP_200_OK)
