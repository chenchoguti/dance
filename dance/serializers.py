from rest_framework import serializers
from django.contrib.auth.decorators import login_required
from .models import Bailarina, Teatro, Show, Nacionalidad

#@login_required
class BailarinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bailarina
        fields = '__all__'

#@login_required
class TeatroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teatro
        fields = '__all__'

#@login_required
class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'


class NacionalidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nacionalidad
		fields = '__all__'