from django.shortcuts import render
from rest_framework import status
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView


from shop.models import Category
from shop.serializers import CategorySerializer


def home(request):
    category = Category.objects.all()
    return render(request, 'index.html', context={'category': category})


class HomeApi(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class HomeMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

