from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password', 'username', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  # Remove confirm_password from validated data
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    #attrs is an incoming dictionary with data to be validated
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username = username, password = password)
        
        if user:
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled")
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError("Invalid email or password. Please try again.")