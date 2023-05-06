from rest_framework import serializers
from .models import UserImage, User
from .utils import send_activation_code



class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'password_confirm')

    def validate(self, attrs):
        # ATTRS BEFORE -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345'), ('password_confirm', '12345')])
        pass1 = attrs.get("password")
        pass2 = attrs.pop("password_confirm")
        # ATTRS AFTER POP -> # ATTRS -> OrderedDict([('email', 'admin1@gmail.com'), ('phone', '996700071102'), ('password', '12345')])
        if pass1 != pass2:
            raise serializers.ValidationError("Passwords do not match!")
        return attrs

    def validate_email(self, email):
        # EMAIL -> admin2@gmail.com
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists")
        return email

    def create(self, validated_data):
        # VALIDATED_DATA -> {'email': 'admin3@gmail.com', 'phone': '996700071102', 'password': '12345'}

        user = User.objects.create_user(**validated_data)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'

    def _get_image_url(self, obj):
        # чтобы сслыка на изображение перекидывалаа на саму фотографию создаем данный метод
        if obj.image: # если есть изображение, то сработает код ниже
            url = obj.image.url #????
            request = self.context.get('request')
            #context содержит в себе словарь со всеми данными
            # из него вытаскиваем значения по ключу request, который мы создали в serializer
            if request is not None:
                url = request.build_absolute_uri(url) #
            else:
                url = ''
            return  url

    def to_representation(self, instance):
        #instance - объект PostImage
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation
    


