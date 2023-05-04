from rest_framework import serializers

from product.models import Product
# from product.serializers import ProductSerializer
from .models import Cart, Cartitems

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(many=False)
    sub_price = serializers.SerializerMethodField(method_name="total")
    class Meta:
        model= Cartitems
        fields = ["id", "cart", "product", "quantity", "sub_price"]

    # def validate(self, attrs):
    #     super().validate(attrs)
    #     attrs['user'] = self.context['request'].user
    #     return attrs
    #
    # def to_representation(self, instance):
    #     #хотим внести доп инфу в блок user
    #     rep = super().to_representation(instance)
    #     rep['user'] = {
    #         'id': instance.user.id,
    #         'email': instance.user.email,
    #     }
    #     return rep

    def total(self, cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ["id", "items", "grand_total"]
    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        #хотим внести доп инфу в блок user
        rep = super().to_representation(instance)
        rep['user'] = {
            'id': instance.user.id,
            'email': instance.user.email,
            'phone': instance.user.phone,
        }
        return rep

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total