from rest_framework import serializers
from test_app.models import UnionBoard
from test_app.models import AuctionBoard


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionBoard
        fields = '__all__'

        
class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionBoard
        fields = '__all__'
