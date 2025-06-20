from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lance, Item

@receiver(post_save, sender=Lance)
def atualizar_valor_item(sender, instance, created, **kwargs):
    if created:
        item = instance.item
        if item.valorAtual is None or instance.valor > item.valorAtual:
            item.valorAtual = instance.valor
            item.save()