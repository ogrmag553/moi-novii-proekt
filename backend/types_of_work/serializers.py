from rest_framework import serializer
from .models import Category,Product


# class CategorySerializer(serializer.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ServiceTypeSerializer(serializer.ModelSerializer):
#     class Meta:
#         model = ServiceType
#         fields = '__all__'

# class PartOrderltemSerializer(serializer.ModelSerializer):
#     class Meta:
#         model = PartOrderltem
#         fields = '__all__'
        


class CategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class SimpleUserSerializer(serializer.ModelSerializer):
    id = serializer.IntegerField()
    username = serializer.CartField()
    email = serializer.EmailField()

class ProductSerializer(serializer.ModelSerializer):
# вкладывваем данные владельца
#если мы вкладываем в класс сериализатора новые данные других сериализеров,тоесть помещаем новые словарики основного словаря
мы обязаны передать их до объявления класса Меттф
после объявления класса  М
