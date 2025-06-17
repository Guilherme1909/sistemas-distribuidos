from rest_framework import serializers
from .models import Item, Lance

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        # Ou se quiser campos específicos:
        # fields = ['id', 'created_on', 'updated_on', 'name', 'description']

class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = '__all__'
        # Ou se quiser campos específicos:
        # fields = ['id', 'created_on', 'updated_on', 'name', 'description']