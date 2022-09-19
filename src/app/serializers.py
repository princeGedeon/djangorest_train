from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):

    url=serializers.HyperlinkedIdentityField(view_name="detail",lookup_field="pk")
    email=serializers.EmailField(write_only=True)
    name=serializers.CharField()
    class Meta:
        model=Product
        fields=['id',"name","content","price","discount","url","email"]

    def validate_name(self,value):
        qs=Product.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Ce champs existe déja")
        return value

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
