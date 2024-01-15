from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
class CreateUpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        read_only_fields = ('author',)


class ListRetrivePostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        read_only_fields = ('author',)
