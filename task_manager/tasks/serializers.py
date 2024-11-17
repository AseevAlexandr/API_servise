from rest_framework import serializers
from .models import Tasks, User
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User.objects.create(**validated_data, password=hashed_password)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.password = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'