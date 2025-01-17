from rest_framework import serializers

from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise ValidationError({'password':'Do not match'})
        
        user.set_password(password)
        user.save()
        return user

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'lat', 'lon', 'provide', 'occupation', 'address']


class SeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['seek_text']