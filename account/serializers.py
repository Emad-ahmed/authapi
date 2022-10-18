from dataclasses import fields
from rest_framework import serializers
from account.models import User


class userRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_Kwargs = {
            'password': {'write_only': True}
        }
