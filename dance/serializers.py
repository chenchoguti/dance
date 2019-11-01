from rest_framework import serializers
from .models import Bailarina, Teatro, Show
class BailarinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bailarina
        fields = '__all__'


class TeatroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teatro
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'