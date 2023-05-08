from rest_framework import serializers
from user_account.serializers import RegisterUserSerializer
from product.models import Product
from .models import Cart, Cartitems, Payment
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

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
    # cart_222 = CartItemSerializer(many=True)
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        # validated_data = self.context.get('request').user
        user = self.context.get('request').user
        # user_obj = get_object_or_404(User, )
        # print('USER', self.context.get('request').user)
        # p = Cart.objects.filter(user=self.context.get('request').user)
        # validated_data['p'] = p
        # validated_data.pop('user')
        # print(validated_data)
        return super().create(validated_data)

    def validate_paid(self, value):
        if value == True:
            raise serializers.ValidationError("Покупка уже оплачена!")
        return value

    def validate_card_number(self, attrs):
        # ATTRS BEFORE -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345'), ('password_confirm', '12345')])
        card = attrs.get("card_number")
        # ATTRS AFTER POP -> # ATTRS -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345')])
        if len(card) != 16:
            raise serializers.ValidationError("Длина пароля от карточки должна быть 16 символов")
        elif card.isalpha():
            raise serializers.ValidationError("Пароль от карточки должен содержать только цифры")
        else:
            super().validate(attrs)
            return attrs

    def validate_cvv(self, attrs):
        cvv = attrs.get("cvv")
        if len(cvv) != 3:
            raise serializers.ValidationError("Длина CVV должна составлять 3 символа")
        elif cvv.isalpha():
            raise serializers.ValidationError("Пароль от CVV должен содержать только цифры")
        else:
            super().validate(attrs)
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