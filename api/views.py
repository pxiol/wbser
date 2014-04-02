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
from spyne.model.binary import File
from spyne.model.primitive import Unicode
from api.models import Reseller

from django.conf import settings

class ResellerContractSign

class ResellerContractVerify

class ResellerContractGetInfo

class ResellerContractListUser

class ResellerContractSOAP(ServiceBase):
	
	@rpc(string, boolean)
	def sign (self, snid, taxpayer_id, contract = True):
		   self.is_valid = False
		   return

    @rpc(string, string, string)
	def verify_user (self, snid, authentication_token, taxpayer_id):
		   self.is_valid = False
           return   

    @rpc(string, string)   
	def get_info (self, snid):

    @rpc(string, string)
	def get_resellerUsers (self, authentication_token, snid):
		return  
	
