from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Cart, Payment
from .serializers import CartSerializer, PaymentSerializer  # PaymentSerializer
from rest_framework.response import Response


# Create your views here.

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class PaymentViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # @swagger_auto_schema(request_body=PaymentSerializer())
    # def post(self, request):
    #     serializer = PaymentSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response("Вы успешно оплатили покупку!", status=201)

