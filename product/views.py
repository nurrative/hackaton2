from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Product, Subcategory
from .serializers import ProductSerializer, SubcategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
