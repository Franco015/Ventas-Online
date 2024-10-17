from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoList.as_view(), name='producto-list'),
    path('productos/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'),
]