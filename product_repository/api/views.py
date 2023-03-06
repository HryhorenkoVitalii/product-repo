from api.tasks import upload_logo
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['modified']

    def perform_create(self, serializer):
        product = serializer.save()
        upload_logo.delay(product.uuid)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.modified:
            return Response({'success': False, 'error': 'Product already updated'},
                            status=status.HTTP_400_BAD_REQUEST)
        instance.modified = True
        instance.save()
        return super().update(request, *args, **kwargs)
