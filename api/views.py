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
	
	@rpc()
	def sig
	def verify_user
	def get_info
	def lget_resellerUsers
	
