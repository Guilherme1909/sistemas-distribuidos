from rest_framework import serializers
from .models import Item, Lance

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = '__all__'
    def validate_valor(self, valor):
        item = self.initial_data.get('item')
        if not item:
            raise serializers.ValidationError("Item inválido.")

        # Pega o objeto Item pelo ID para verificar valorFinal
        try:
            item_obj = Item.objects.get(pk=item)
        except Item.DoesNotExist:
            raise serializers.ValidationError("Item não encontrado.")

        if item_obj.valorFinal is not None and valor > item_obj.valorFinal:
            raise serializers.ValidationError(
                f"O lance não pode ser maior que o valor máximo do item: {item_obj.valorFinal}"
            )
        return valor