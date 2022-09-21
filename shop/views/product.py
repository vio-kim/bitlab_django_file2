from rest_framework import mixins
from rest_framework.generics import GenericAPIView


from shop.models import Product
from shop.serializers import ProductCreateAndListSerializer
from shop.serializers import ProductSerializer


class ProductDetailMixin(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductMixin(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateAndListSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
