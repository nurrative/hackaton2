from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Product, Subcategory
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, SubcategorySerializer
from rest_framework.filters import SearchFilter

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('name', 'description', 'subcategory')

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
