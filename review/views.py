from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsAuthor


from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class =  CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     like, created = Like.objects.get_or_create(user=request.user, post=post)
#     if not created:
#         like.delete()
#     return HttpResponse()