from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city'] #'card_number', 'cvv'

    # def validate(self, attrs):
    #     # но нам нужно добавить поле user в наш словарь с данными, поэтому переопределяем функцию validate
    #     super().validate(attrs)
    #     attrs['user'] = self.context['request'].user
    #     return attrs

    # def to_representation(self, instance):
    #     #хотим внести доп инфу в блок user
    #     rep = super().to_representation(instance)
    #     rep['user'] = {
    #         'id': instance.user.id,
    #         'email': instance.user.email,
    #     }
    #     return rep
