from posixpath import basename
from django.urls import path
from rest_framework.routers import DefaultRouter
from .models import BlogPost 

from .views import BlogPostViewSet

router = DefaultRouter()
router.register(r'BlogPost', BlogPostViewSet, basename= 'BlogPost')
urlpatterns = [] + router.urls