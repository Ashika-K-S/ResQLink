from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_password(self, value):
        from django.contrib.auth.password_validation import validate_password
        validate_password(value)
        return value

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'phone')

    
    def validate_role(self, value):
        if value == 'authority':
            raise serializers.ValidationError(
                "Authority role cannot be assigned during registration"
            )
        return value

    
    def validate(self, data):
        if not data.get('username'):
            raise serializers.ValidationError("Username is required")

        return data

    
    def create(self, validated_data):
        role = validated_data.pop('role', 'citizen')

        user = User.objects.create_user(
            role=role,
            is_role_set=True,
            **validated_data
        )

        return user