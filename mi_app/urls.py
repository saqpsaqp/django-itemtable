from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='listar_items'),
    path('agregar/', views.ItemCreateView.as_view(), name='agregar_item'),
    path('editar/<int:pk>/', views.ItemUpdateView.as_view(), name='editar_item'),
    path('eliminar/<int:pk>/', views.ItemDeleteView.as_view(), name='eliminar_item'),
    path('cambiar_estado/<int:pk>/', views.ItemDeleteView.as_view(), name='cambiar_estado'),  # Nueva URL para el cambio de estado
]