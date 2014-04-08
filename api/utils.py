class ResellerContract:
	
	def __init__:
		
		
	def get_info(self, snid):
		try:
			reseller = Reseller.objects.get(id=snid)
		except:
			self.is_valid = False
			return 
			
		return {name:rseller.name, telephone:'31412541', email:reseller.email}
		
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

        #authentitation_token
	 def verify_user ( self, snid, taxpayer_id):

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
       	return {success:True}

        #authentication_token
     def get_resellerUsers( self, snid, taxpayer_id, contract):

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
          		reseller_user = ResellerUserInvoice.objects.filter(reseller=reseller, taxpayer_id= taxpayer_id, snid = snid, name = name, telephone= telephone, address= address, email= email, estado = estado)
            except:
                self.is_valid = False
                retunr
            reseller_user.contract = contract
            reseller_user.save()
            return {success:True}		



        	


