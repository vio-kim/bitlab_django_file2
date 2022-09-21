from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    category = CategorySerializer


class ProductCreateAndListSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('title', 'price', 'category_id', )

    def validate(self, attrs):
        price = attrs.get('price', 0)
        if price <=0:
            raise ValidationError('price might be higher than 0')
        return attrs
