from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .email_service import enviar_email_confirmacao
from .serializers import AdocaoSerializer
from .models import Adocao


class AdocaoList(APIView):
    def get(self, req, format=None):
        adocoes = Adocao.objects.all()
        serializer = AdocaoSerializer(adocoes, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, req, format=None):
        deserializer = AdocaoSerializer(data=req.data)
        if deserializer.is_valid():
            adocao = deserializer.save()
            enviar_email_confirmacao(adocao)
            return Response(deserializer.data, status=HTTP_201_CREATED)
        else:
            return Response(
                {
                    "errors": deserializer.errors,
                    "message": "Houveram erros de validação",
                },
                status=HTTP_400_BAD_REQUEST,
            )
