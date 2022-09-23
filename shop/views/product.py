from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from shop.models import Product
from shop.serializers import ProductCreateAndListSerializer
from shop.serializers import ProductSerializer


class ProductDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            try:
                instance = self.queryset.get(id=pk)
                serializer = self.serializer_class(instance)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(data={'ERROR': 'by given pk object not found!'},
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductMixin(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateAndListSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
