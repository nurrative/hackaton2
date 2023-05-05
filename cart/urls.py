from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, PaymentView

router = DefaultRouter()
router.register('cart', CartViewSet)
# router.register('cartitems', CartitemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payment/', PaymentView.as_view()),
]