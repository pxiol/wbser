# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
#logging.basicConfig(filename='/tmp/wis-services.log', level=logging.DEBUG)

from spyne.model.primitive import String
from spyne.model.primitive import Boolean
from spyne.model.complex import Array
from spyne.model.complex import ComplexModel
from spyne.service import ServiceBase
from spyne.decorator import srpc
#from spyne.model.binary import File
from spyne.model.primitive import Unicode
from api.models import Reseller

from django.conf import settings

class ResellerContractSOAP(ServiceBase):
		
	@rpc(String, Boolean)
	def sign (self, snid, taxpayer_id, authentication_token, contract):    #verificar si va True el contract.

		   self.is_valid = False
		   return

    @srpc(String, String, String)
	def verify_user (self, snid, authentication_token, taxpayer_id):
		   self.is_valid = False
           return   

    @rpc(String, String)   
	def get_info (self, snid, contract): 
           return 

    @srpc(String, String)
	def get_resellerUsers (self, authentication_token, snid):
		   return  

	
