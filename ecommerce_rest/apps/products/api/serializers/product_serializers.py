from apps.products.models import Product

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
