from rest_framework import viewsets
from .products import create, list_all


class Products(viewsets.ModelViewSet):

    def create(self, request):
        return create(request.data)

    def list(self, request):
        return list_all()    