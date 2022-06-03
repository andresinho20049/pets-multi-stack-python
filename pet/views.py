from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Pet
from .serializers import PetSerializers

class PetList(APIView):
    def get(self, req, format=None):
        pets = Pet.objects.all()
        serializer = PetSerializers(pets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)