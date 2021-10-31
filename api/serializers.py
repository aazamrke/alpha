from rest_framework.serializers import ModelSerializer

from api.models import Quote


class QuoteSerializers(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


