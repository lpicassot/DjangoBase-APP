from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter
from .views import ProductView, SearchCoordsView

urlpatterns = [
    path('products', ProductView.as_view()),
    path('searchcoords', SearchCoordsView.as_view())
]