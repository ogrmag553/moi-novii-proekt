from rest_framework import serializer
from .models import Category,ServiceType,PartOrderltem

class CategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ServiceTypeSerializer(serializer.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

class PartOrderltemSerializer(serializer.ModelSerializer):
    class Meta:
        model = PartOrderltem
        fields = '__all__'
        

