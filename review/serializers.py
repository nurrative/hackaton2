from rest_framework.serializers import ModelSerializer
from .models import Comment
# Rating, Favorite

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # exclude = ('user',)
        fields = '__all__'
        #так как наше поле user должен автоматичеки заполняться, то надо включить его в переменную exclude
    def validate(self, attrs):
        # но нам нужно добавить поле user в наш словарь с данными, поэтому переопределяем функцию validate
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        #хотим внести доп инфу в блок user
        rep = super().to_representation(instance)
        rep['user'] = {
            'id': instance.user.id,
            'email': instance.user.email,
        }
        return rep