from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Timecard
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TimecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timecard
        fields = ('id', 'user', 'date', 'start_time', 'end_time',
                  'lunch', 'sick_day', 'int_hours', 'ext_hours')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = self.create_auth_token()
        user.save()
        return user
