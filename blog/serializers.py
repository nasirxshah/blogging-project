from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "created_at", "updated_at"]

    def create(self, validated_data):
        blogpost = BlogPost(**validated_data)
        blogpost.author = self.context.get("user")
        blogpost.save()

        return blogpost
