from app.models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

def validate_name(value):
    qs=Product.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError('Ce nom existe déja')
    return value

validate_unique_name=UniqueValidator(queryset=Product.objects.all())