from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Product
from .serializers import CategorySerializers, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializers
    
    @action(detail=True, methods=['get'])
    def product(self, request, pk=None):
        product = Product.objects.filter(
            categories__id= pk
        )
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    
    @action(detail=True, methods=['get'])
    def category(self, request, pk=None):
        category = Category.objects.filter(
            product__id= pk
        )
        serializer = CategorySerializers(category, many=True,)
        return Response(serializer.data)


#class CategoryViewSet(viewsets.ViewSet):
#    def list(self, request):
#        queryset = Category.objects.all()
#        serializer = CategorySerializers(queryset, many=True)
#        return Response(serializer.data)
#
#    def retrieve(self, request, pk=None):
#        queryset = Category.objects.all()
#        category = get_object_or_404(queryset, pk=pk)
#        serializer = CategorySerializers(category)
#        return Response(serializer.data)
    