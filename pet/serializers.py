from dataclasses import fields
from rest_framework import serializers

from .models import Pet

class PetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'nome', 'historia', 'foto')