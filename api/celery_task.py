import os
from celery import Celery
from django.contrib.sites import requests
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpha.settings')

app = Celery('alpha')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
from rest_framework.response import Response


@app.task(bind=True)
def get_bitcoin_exchange(*args, **kwargs):
  from api.serializers import QuoteSerializers
  try:
    apikey = os.environ.get('APIKEY')
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={apikey}'
    r = requests.get(url)
    response = r.json()

    data = response['Realtime Currency Exchange Rate']

    btc = {
        'from_currency_code': data['1. From_Currency Code'],
        'from_currency_name': data['2. From_Currency Name'],
        'to_currency_code': data['3. To_Currency Code'],
        'to_currency_name': data['4. To_Currency Name'],
        'exchange_rate': data['5. Exchange Rate'],
        'last_refreshed': data['6. Last Refreshed'],
        'time_zone': data['7. Time Zone'],
        'bid_price': data['8. Bid Price'],
        'ask_price': data['9. Ask Price']
    }

    serializers = QuoteSerializers(data=btc)
    if serializers.is_valid():
        serializers.save()
        return serializers.data, True
  except:
        return Response({"error": "Invalid Request"}, status=HTTP_400_BAD_REQUEST)
