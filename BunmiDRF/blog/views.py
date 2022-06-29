from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BlogPostSerializer
from .models import BlogPost

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
