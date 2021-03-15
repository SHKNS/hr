from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from test_app.models import UnionBoard, OverseeBoard
from test_app.models import FmBoard, PpBoard,CoolBoard, RuliBoard
from test_app.models import AuctionBoard, CoupangBoard, ElevenBoard, GmarketBoard


from test_app.serializers import TestSerializer, OverseeSerializer
from test_app.serializers import FmSerializer, PpSerializer, CoolSerializer, RuliSerializer
from test_app.serializers import AuctionSerializer, CoupangSerializer, ElevenSerializer, GmarketSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = UnionBoard.objects.all() 
    serializer_class = TestSerializer

class OverseeViewSet(viewsets.ModelViewSet):
    queryset = OverseeBoard.objects.all() 
    serializer_class = OverseeSerializer  
    
#########################################################################    

class FmViewSet(viewsets.ModelViewSet):
    queryset = FmBoard.objects.all() 
    serializer_class = FmSerializer
    
class PpViewSet(viewsets.ModelViewSet):
    queryset = PpBoard.objects.all() 
    serializer_class = PpSerializer            
    
class CoolViewSet(viewsets.ModelViewSet):
    queryset = CoolBoard.objects.all() 
    serializer_class = CoolSerializer
    
class RuliViewSet(viewsets.ModelViewSet):
    queryset = RuliBoard.objects.all() 
    serializer_class = RuliSerializer
    
    
    
#########################################################################    

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = AuctionBoard.objects.all() 
    serializer_class = AuctionSerializer
    
class CoupangViewSet(viewsets.ModelViewSet):
    queryset = CoupangBoard.objects.all() 
    serializer_class = CoupangSerializer            
    
class ElevenViewSet(viewsets.ModelViewSet):
    queryset = ElevenBoard.objects.all() 
    serializer_class = ElevenSerializer
    
class GmarketViewSet(viewsets.ModelViewSet):
    queryset = GmarketBoard.objects.all() 
    serializer_class = GmarketSerializer
    
    
    