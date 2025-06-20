from django.shortcuts import render, get_object_or_404
from .models import Item, Lance
from rest_framework import viewsets
from .serializer import ItemSerializer, LanceSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class LanceViewSet(viewsets.ModelViewSet):
    queryset = Lance.objects.all()
    serializer_class = LanceSerializer
    

def home(request):
    itens = Item.objects.all()
    return render(request, 'leiloes/home.html', {'itens': itens})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'leiloes/item_detail.html', {'item': item})