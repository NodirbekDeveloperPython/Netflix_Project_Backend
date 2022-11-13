from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import *


class AktyorlarSerializer(ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'
    def validate_jins(self, value):
        if value.lower() != 'erkak' and value.lower() != 'ayol':
            raise ValidationError("Jinsga siz bergandek qiymat kiritib bo'lmaydi Janob.")
        return value

class KinolarSerializer(ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Izohlar
        fields = '__all__'

class IzohSerialzier(ModelSerializer):
    class Meta:
        model = Izohlar
        fields = '__all__'