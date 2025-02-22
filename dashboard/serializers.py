from rest_framework import serializers
from .models import Product, Sale, Stock, User, Offer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        field = '__all__'

class SaleSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Sale 
        field = '__all__

class StockSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Stock 
        field = '__all__'

class UserSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = User 
        field = '__all__'

class OfferSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Offer 
        field = '__all__'