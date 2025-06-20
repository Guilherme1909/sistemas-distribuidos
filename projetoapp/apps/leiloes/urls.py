from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'leiloes'

router = routers.DefaultRouter()
router.register(r'Itens', views.ItemViewSet, basename='itens')
router.register(r'Lances', views.LanceViewSet, basename='lances')

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('api/', include(router.urls)),
]