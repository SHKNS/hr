from rest_framework import serializers
from test_app.models import UnionBoard, OverseeBoard
from test_app.models import FmBoard, PpBoard, CoolBoard, RuliBoard
from test_app.models import AuctionBoard, CoupangBoard, ElevenBoard, GmarketBoard


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionBoard
        fields = '__all__'
                
class OverseeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverseeBoard
        fields = '__all__'       
    
#########################################################################    
    
class FmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FmBoard
        fields = '__all__'   
        
class PpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PpBoard
        fields = '__all__'   
        
class CoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoolBoard
        fields = '__all__'   
        
class RuliSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuliBoard
        fields = '__all__'   
        
        
        
#########################################################################    
        
class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionBoard
        fields = '__all__'   

class CoupangSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoupangBoard
        fields = '__all__'           
        
class ElevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevenBoard
        fields = '__all__'         
                                
class GmarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = GmarketBoard
        fields = '__all__'
