from rest_framework import serializers
from .models import User, Timecard
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TimecardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Timecard
    fields = ('id', 'user', 'date', 'start_time', 'end_time', 'lunch', 'sick_day', 'int_hours', 'ext_hours')


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password')
    extra_kwargs = {'password': {'write_only': True, 'required': True}}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    token = Token.objects.create(user=user)
    return user
