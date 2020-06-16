from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User, Timecard
from .serializers import TimecardSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TimecardViewSet(viewsets.ModelViewSet):
    queryset = Timecard.objects.all()
    serializer_class = TimecardSerializer
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated)
