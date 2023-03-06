from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField() 

    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'logo']
