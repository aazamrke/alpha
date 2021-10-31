from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.celery_task import get_bitcoin_exchange
from api.models import Quote
from api.serializers import QuoteSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.status import *

class Quotes(viewsets.ModelViewSet):
    serializer_class = QuoteSerializers
    queryset = Quote.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['exchange_rate', 'bid_price', 'ask_price', 'last_refreshed']

    def create(self, request, *args, **kwargs):
        try:
            data, code = get_bitcoin_exchange()
            if code:
                return Response(data, status=HTTP_200_OK)
        except:
                return Response(data, status=HTTP_400_BAD_REQUEST)
