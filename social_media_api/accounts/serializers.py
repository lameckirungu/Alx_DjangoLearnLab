from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "bio", "first_name", "last_name"]
        read_only_fields = ["id"]        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
class RegisterSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ["id", "username", "bio", "first_name", "last_name", "password"]
        extra_kwargs = {
             "password": {"write_only": True, "min_length": 8}
        } 

    def create(self, validated_data):
            return User.objects.create_user(**validated_data)
    

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "bio", "created_at"]

     