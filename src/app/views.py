from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Product

from app.serializers import ProductSerializer


@api_view(['GET'])
def product_all(request):
    query=Product.objects.all()
    data={}
    if query:
        data=ProductSerializer(query,many=True).data
    return Response(data)

@api_view(['POST'])
def add_product(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        return Response(serializer.data)
    else:
        return Response({"detail":"invalid"})