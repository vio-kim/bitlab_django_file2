from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from shop.models import Category, Product

from .category import CategorySerializer


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    category = CategorySerializer
    publish_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.category = validated_data.get("category", instance.category)
        instance.publish_date = validated_data.get("publish_date", instance.publish_date)
        instance.save()
        return instance


class ProductCreateAndListSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('title', 'price', 'category_id', )

    def validate(self, attrs):
        price = attrs.get('price', 0)
        if price <= 0:
            raise ValidationError('price might be higher than 0')
        return attrs

