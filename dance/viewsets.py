from rest_framework import viewsets 
from .models import Bailarina, Teatro, Show
from .serializers import BailarinaSerializer, TeatroSerializer, ShowSerializer 
class BailarinaViewSet (viewsets.ModelViewSet): 
    queryset = Bailarina.objects.all () 
    serializer_class = BailarinaSerializer


class TeatroViewSet (viewsets.ModelViewSet): 
    queryset = Teatro.objects.all () 
    serializer_class = TeatroSerializer


class ShowViewSet (viewsets.ModelViewSet): 
    queryset = Show.objects.all () 
    serializer_class = ShowSerializer

