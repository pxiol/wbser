from django.conf.urls import patterns, include, url
from spyne.server.django import DjangoView
from api.views import ResellerContractSOAP
from spyne.protocol.soap import Soap11

urlpatterns = patterns('',
 url(r'^wbser/', DjangoView.as_view(
   services=[ResellerContractSOAP], tns='ResellerContractSOAP',
   in_protocol=Soap11(), out_protocol=Soap11())),

 )