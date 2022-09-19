from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Product

from app.serializers import ProductSerializer,CreateProductSerializer

from rest_framework import generics

class DetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    def perform_create(self, serializer):

        content="C'est vide"

        serializer.save(content=content)

class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    def perform_create(self, serializer):

        content="C'est vide"

        serializer.save(content=content)


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    def perform_update(self, serializer):
        content=serializer.validated_data.get('content') or None
        if content is None:
            content="Vide"
        serializer.save(content=content)

class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"