from api.models import Reseller
from api import ResellerInvoice
from api import ResellerUser
from api.models import ResellerUserInvoice
from django.conf import settings 
#from apps.invoicing.models import Account
#from django.contrib.auth.models import User
from datetime import datetime
from datetime import timedelta
#from settings import authentication_token


class authentiaton:(object)

   Authentication_token = 1
   
class ResellerContract:(object)



	def get_SNInfo(self, snid, authentication_token):

    try:
      reseller = Reseller.objects.get(id=snid)

    except:
      self.is_valid = False
      return 
      
    return {taxpayer_id:reseller.taxpayer_id, name:reseller.name, telehone:'31412541', email:reseller.email, addres:reseller.addres}

#Authentication_token
  def verify_user (self, snid, taxpayer_id, authentication_token):

    try:
      reseller = Reseller.objects.get(id=snid)

      except:
        self.is_valid = False
        return

      if reseller.type == 'U':
        try:
          reseller_user == ReresellerUser.objects.filter(reseller=reseseller, taxpayer_id=taxpayer_id, snid=snid)
        except:
          self.is_valid = False
          return
      
      elif reseller.type == 'I':
        try:

            reseller = Reseller.objects.get(id=snid)

       	except:
       		self.is_valid = False
       		return

       	if reseller.type ==  'U':
       		try:
       			reseller_user == ResellerUser.objects.filter(reseller=reseller, taxpayer_id=taxpayer_id, snid=snid)
       		except:
       			self.is_valid = False
       			return
       	elif reseller.type =='I':
       		try:
       			resseller_user = ResellerUserInvoice.objects.filter(reseller=reseller, taxpayer_id=taxpayer_id, snid=snid)
       		except:
       			self.is_valid=False
      
       			return
            
       	reseller_user.success =success
       	reseller_user.contract=contract
       	reseller_user.save()
       	return {success:True or False, contract: True or False}

   
 
#Authentication_token
  def sign_contract(self, snid, taxpayer_id, contract=True, authentication_token):

    try:
      reseller = Reseller.objects.get(id=snid)
    except:
      self.is_valid = False
      return 
      
    if reseller.type == 'U':
      try:
        reseller_user = ResellerUser.objects.filter(reseller=reseller, taxpayer_id=taxpayer_id)
      except:
        self.is_valid = False
        return 
    elif reseller.type == 'I':
      try:
        reseller_user = ResellerUserInvoice.objects.filter(reseller=reseller, taxpayer_id=taxpayer_id)
      except:
        self.is_valid = False
        return 
    reseller_user.contract = contract
    reseller_user.save()
    return {succes:True or False}

   #authentication_token
     def get_resellerUsers( self, snid, taxpayer_id, authentication_token):

      try:
        reseller = Reseller.objects.get( id=snid)
      except:
          self.is_valid = False 
          return

        if resseler.type == 'U':
          try:
            reseller_user == ResellerUser.objects.filter(reseller = reseller, taxpayer_id= taxpayer_id, name = name, telephone= telephone, address= address, email= email, estado = estado)

            except:
              self.is_valid = False
              return
          elif reseller.type == 'I':

            try:
              reseller_user = ResellerUserInvoice.objects.filter(snid = snid)
            except:
                self.is_valid = False
                return

            try:
              reseller_user = ResellerUserInvoice.objects.filter(reseller=reseller, taxpayer_id= taxpayer_id, snid = snid, name = name, telephone= telephone, address= address, email= email, estado = estado)
            except:
                self.is_valid = False
                return  {taxpayer_id: boolean, taxpayer_id: string, contract: boolean }
                                 



      
