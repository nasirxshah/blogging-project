from rest_framework.viewsets import ModelViewSet
from .serializers import BlogPostSerializer
from .models import BlogPost
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class BlogPostViewSet(ModelViewSet):
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return user.blogposts


    def get_serializer_context(self):
        return {"user":self.request.user}