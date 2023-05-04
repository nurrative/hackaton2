from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Cart
from .serializers import CartSerializer


# Create your views here.

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# class CartitemsViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
#     queryset = Cartitems.objects.all()
#     serializer_class = CartItemSerializer
