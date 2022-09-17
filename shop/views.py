from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorySerializer



def home(request):
    category = Category.objects.all()
    return render(request, 'index.html', context={'category': category})


def about(request):
    return render(request, 'about.html')


class HomeApi(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

