from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = '__all__'

    def update(self, instance, validated_data):
        request = self.context.get('request')
        current_user = request.user
        
        if current_user.is_staff:
            validated_data['user'] = instance.user
        

        return super().update(instance, validated_data)