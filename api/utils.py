class ResellerContract:(object)

	 def sign_contract(self, snid, taxpayer_id, contract=True):
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
    return {succes:True}
		
		
	def get_SNID_info(self, snid):
		try:
			reseller = Reseller.objects.get(id=snid)
		except:
			self.is_valid = False
			return 
			
		return {name:reseller.name, telehone:'31412541', email:reseller.email}

	def verify_user(self, snid, )
		

