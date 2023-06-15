from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Product, Category
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, SubcategorySerializer
from rest_framework.filters import SearchFilter
from .permissions import IsAdminOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('name', 'subcategory')
    permission_classes = [IsAdminOrReadOnly]

    def __str__(self) -> str:
        return super().__str__()

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = SubcategorySerializer
