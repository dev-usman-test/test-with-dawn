from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, generics
from .serializers import ProductSerializers
from .models import Product
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
# Create your views here.
def index(request):
    return HttpResponse("ok")

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        queryset = Product.objects.filter(name__icontains = search_term)
        return queryset

class ProductSearch(generics. ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        queryset = Product.objects.filter(name__icontains = search_term)
        return queryset
