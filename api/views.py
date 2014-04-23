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
		
	@srpc(String (encoding='utf8'),String(encoding='utf8'),String(encoding='utf8'),String(enconding='utf8'), Boolean(encoding='utf8'))
	def sign (self, snid, taxpayer_id, authentication_token, contract):    #verificar si va True el contract.

		   self.is_valid = False
		   return

#    @srpc(String(encoding='utf8'),String(encoding='utf8'),String(encoding='utf8'),String(encoding='utf8'), _returns=UserLCOResult)
#	def verify_user (self, snid, authentication_token, taxpayer_id):

#		   self.is_valid = False
#           return   

#    @srpc(String(encoding='utf8'),String(encoding='utf8'),String(encoding='utf8'), _returns=InfoLCOResult)   
#	def get_info (self, snid, contract): 
#
#		   self.is_valid = False
#          return 

#    @srpc(String(encoding='utf8'),String(encoding='utf8'),String(encoding='utf8'), _returns=ResellerUsersCOResult)
#    def get_resellerUsers (self, authentication_token, snid):

#    	   self.is_valid = False
#     	   return  

	
