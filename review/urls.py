from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, AddRatingAPIView

router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/', AddRatingAPIView.as_view()),

]