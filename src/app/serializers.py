from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    dsc=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields=['id',"name","content","price","discount","dsc"]
    def get_dsc(self,obj):
        return obj.discount