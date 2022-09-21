from django.urls import path

from .views import home, HomeApi, HomeMixinApiView, ProductMixin, ProductDetailMixin

urlpatterns = [
    path('', home, name='home'),
    path('category/', HomeApi.as_view()),
    path('category_create/', HomeMixinApiView.as_view()),
    path('products/', ProductMixin.as_view()),
    path('products/<int:pk>/', ProductDetailMixin.as_view()),
]
