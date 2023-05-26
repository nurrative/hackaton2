from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsAuthor
from rest_framework.decorators import api_view

from .models import Comment, Favorite, Rating, Like
from .serializers import CommentSerializer, RatingSerializer, FavoriteSerializer


from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class =  CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

class FavoriteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset =  Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        #пытаемся установить фильтр по Избранным

class RatingViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    # @swagger_auto_schema(request_body=RatingSerializer())
    # def post(self, request):
    #     ser = RatingSerializer(data=request.data, context={'request': request})
    #     ser.is_valid(raise_exception=True)
    #     ser.save()
    #     return Response(ser.data, status=201)
@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    comment = get_object_or_404(Comment, id=id)
    if Like.objects.filter(user=user, comment=comment).exists():
        # Если лайк есть, то удаляем его
        Like.objects.filter(user=user, comment=comment).delete()
    else:
        # если нет, создаем
        Like.objects.create(user=user, comment=comment)
    return Response(status=201)
