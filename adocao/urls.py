from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import AdocaoList

urlpatterns = [path("", AdocaoList.as_view())]
