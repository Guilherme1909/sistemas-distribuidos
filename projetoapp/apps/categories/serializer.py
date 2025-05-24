from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # Ou se quiser campos específicos:
        # fields = ['id', 'created_on', 'updated_on', 'name', 'description']