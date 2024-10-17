from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer