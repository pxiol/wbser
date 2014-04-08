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

class ResellerContractSign

class ResellerContractVerify

class ResellerContractGetInfo

class ResellerContractListUser


class ResellerContractSOAP(ServiceBase):
	
<<<<<<< HEAD
	@srpc(String(encoding='utf8'), String(encoding='utf8'), boolean)
	def sign (self, snid, taxpayer_id, contract = True):
=======
	@rpc(string, boolean)
	def sign (self, snid, taxpayer_id, authentication_token, contract = True):    #verificar si va True el contract.
>>>>>>> 66ce0651899986c6054d082eb05b7738fdc7538d
		   self.is_valid = False
		   return

    @srpc(string, string, string)
	def verify_user (self, snid, authentication_token, taxpayer_id):
		   self.is_valid = False
           return   

<<<<<<< HEAD
    @srpc(String(encoding='utf8'))   
	def get_info (self, snid):
=======
    @rpc(string, string)   
	def get_info (self, snid, contract = True):  #verificar si va True el contract.
>>>>>>> 66ce0651899986c6054d082eb05b7738fdc7538d

    @srpc(string, string)
	def get_resellerUsers (self, authentication_token, snid):
		return  

	
