from .models import Profile
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "bio", "first_name", "last_name", "profile_picture"]
        read_only_fields = ["id"]        
        
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "username", "bio", "first_name", "last_name", "password"]
        extra_kwargs = {
             "password": {"write_only": True, "min_length": 8}
        } 
        
    def create(self, validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="profile.full_name", required=False, allow_blank=True)
    phone_number = serializers.CharField(source="profile.phone_number", required=False, allow_blank=True)
    address = serializers.CharField(source="profile.address", required=True, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "bio", "profile_picture", "full_name", "phone_number", "address"]
        read_only_fields = ["id", "username"]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", {})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
    
        profile, _ = Profile.objects.get_or_create(user=instance)
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance
