from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from shop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
