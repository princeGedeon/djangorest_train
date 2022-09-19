from rest_framework import serializers

from app.models import Product

from app.validators import validate_name


class ProductSerializer(serializers.ModelSerializer):

    url=serializers.HyperlinkedIdentityField(view_name="detail",lookup_field="pk")
    email=serializers.EmailField(write_only=True)
    name=serializers.CharField(validators=[validate_name])
    class Meta:
        model=Product
        fields=['id',"name","content","price","discount","url","email"]



    def create(self, validated_data):
        email=validated_data.pop('email')
        print(email)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.pop('email')
        return super().update(instance,validated_data)


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=["name","content","price"]
