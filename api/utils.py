class ResellerContract:
	
	def __init__:
		
		
	def get_info(self, snid):
		try:
			reseller = Reseller.objects.get(id=snid)
		except:
			self.is_valid = False
			return 
			
		return {name:rseller.name, telehone:'31412541', email:reseller.email}
		
	def sign(self, snid, taxpayer_id, contract=True):
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
		return {success:True}

	 def verify_user ( self, snid, #Authentication_token taxpayer_id):

        try:
            reseller = Reseller.objects.get(id=SNID)

       	except:
       		self.is_valid = False
       		return

       	if reseller.type ==  'U':
       		try:
       			reseller_user == ReresellerUser.objects.filter(reseller=reseseller, taxpayer_id=taxpayer_id, snid=snid)
       		except:
       			self.is_valid = False
       			return
       	elif reseller.type =='I':
       		try:
       			resseller_user = ResellerUserInvoice.objects.filter(reseller=reseller, taxpayer_id=taxpayer_id, snid=snid)
       		except:
       			self.is_valid=False
       			retunr
       	reseller_user.success =success
       	reseller_user.contract=contract
       	reseller_user.save()
       	return {success:True}

     def get_resellerUsers( self, #authentication_token SNID, taxpayer_id, contract):

     	try:
     		reseller = Reseller.objects.get( id=SNID)
     	except:
     	    self.is_valid = False	
     	    return

     	


