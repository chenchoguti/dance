from rest_framework import viewsets 
from django.contrib.auth.decorators import login_required
from .models import Bailarina, Teatro, Show, Nacionalidad
from .serializers import BailarinaSerializer, TeatroSerializer, ShowSerializer, NacionalidadSerializer


#@login_required
class BailarinaViewSet (viewsets.ModelViewSet): 
	queryset = Bailarina.objects.all () 
	serializer_class = BailarinaSerializer



#login_required
class TeatroViewSet (viewsets.ModelViewSet): 
    queryset = Teatro.objects.all () 
    serializer_class = TeatroSerializer

#@login_required
class ShowViewSet (viewsets.ModelViewSet): 
    queryset = Show.objects.all () 
    serializer_class = ShowSerializer

class NacionalidadViewSet(viewsets.ModelViewSet):
	queryset = Nacionalidad.objects.all()
	serializer_class = NacionalidadSerializer