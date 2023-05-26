from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, RatingViewSet, FavoriteViewSet
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('favorites', FavoriteViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('rating/', AddRatingAPIView.as_view()),

# ]
