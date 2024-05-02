from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
