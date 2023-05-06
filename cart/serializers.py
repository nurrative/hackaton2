from rest_framework import serializers

from product.models import Product
# from product.serializers import ProductSerializer
from .models import Cart, Cartitems, Payment  # Payment


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

class PaymentSerializer(serializers.ModelSerializer):
    # payments = CartSerializer(many=False)


    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        payment = super().create(validated_data)
        payment.set_password(validated_data['password'])
        payment.save()
        return payment

    def validate(self, attrs):
        # ATTRS BEFORE -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345'), ('password_confirm', '12345')])
        card = attrs.get("card_number")
        # ATTRS AFTER POP -> # ATTRS -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345')])
        if len(card) != 16:
            raise serializers.ValidationError("Длина пароля от карточки должна быть 16 символов")
        super().validate(attrs)
        attrs['cart'] = self.context['request'].cart
        # else:
        #     cart = Cart(request)
        return attrs

    # def validate(self, attrs):
    #     super().validate(attrs)
    #     attrs['user'] = self.context['request'].user
    #     return attrs

    # def to_representation(self, instance):
    #     #хотим внести доп инфу в блок user
    #     rep = super().to_representation(instance)
    #     rep['cart'] = {
    #         "id": instance.cart.id,
    #         "items": instance.cart.items,
    #         "grand_total": instance.cart.grand_total,
    #     }
    #     return rep



    # def update(self, instance, validated_data):
    #     payment = super().update(instance, validated_data)
    #     try:
    #         payment.set_password(validated_data['password'])
    #         payment.save()
    #     except KeyError:
    #         pass
    #     return payment