from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Product

from app.serializers import ProductSerializer,CreateProductSerializer

from  rest_framework import permissions,authentication
from rest_framework import generics,mixins

from app.permissions import IsStaffPermission

from app.permissions_mixins import EditorUserPermissionsMixin


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

class ListCreateApiView(generics.ListCreateAPIView,EditorUserPermissionsMixin):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStaffPermission]
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


#Les mixins
class ProductMixinView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_update(self, serializer):
        content=serializer.validated_data.get('content') or None
        if content is None:
            content="Vide"
        serializer.save(content=content)




