from rest_framework import serializers
from .models import Product, Category, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        return rep


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

    def _get_image_url(self,obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')


class SubcategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
