from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from accounts.models import Role, User


class UserSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=122)
    last_name = serializers.CharField(max_length=122)
    role = serializers.ChoiceField(choices=Role)
    description = serializers.CharField(max_length=500)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.role = self.data.get('role')
        user.description = self.data.get('description') 
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'role',
            'description',
        )
        read_only_fields = ('pk', 'username', 'email', 'first_name', 'last_name')


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)