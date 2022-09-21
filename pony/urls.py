from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.HomeApi.as_view()),
    path('category_create/', views.HomeMixinApiView.as_view()),
    path('products/', views.ProductMixin.as_view()),
    path('products/<int:pk>/', views.ProductDetailMixin.as_view()),
]
