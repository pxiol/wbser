from django.db import models

INVOICE_TYPES = (
    ('I', 'Internal'),
    ('E', 'External'),
    ('0', 'Outer'),
)

RESELLER_TYPES = (
    ('I', 'Per Invoice'),
    ('U', 'Per User'),
)

RESELLER_STATUS = (
    ('A', 'Active'),
    ('S', 'Suspended'),
)

RESELLERUSER_STATUS = (
    ('A', 'Active'),
    ('S', 'Suspended'),
    ('P', 'Pending'),
)

INVOICE_STATUS = (
    ('S', 'Signed'),
    ('F', 'Finished'),
    ('C', 'Cancelled'),
    ('P', 'Pending'),
)

BILLING_STATUS = (
    ('P', 'Paid'),
    ('E', 'Pending'),
    ('S', 'Suspended'),
    ('A', 'Active'),
)


class Reseller(models.Model):
  #profile = models.ForeignKey('core.UserProfile')
  name = name = models.CharField(max_length=255)
  username = models.CharField(max_length=60)
  password = models.CharField(max_length=255)
  passphrase = models.CharField(max_length=255)
  type = models.CharField(max_length=1, choices=RESELLER_TYPES, default='I')  
  pricing = models.FloatField(default=0.00)
  coupon_allowed = models.BooleanField(default=False)
  status = models.CharField(max_length=1, choices=RESELLER_STATUS, default='A')
  #pending_billing = models.PositiveIntegerField(max_length=10, default=0)

class ResellerUser(models.Model):
  reseller = models.ForeignKey('Reseller')
  taxpayer_id = models.CharField(max_length=14)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  next_billing = models.DateField(null=True, blank=True)
  status = models.CharField(max_length=1, choices=RESELLERUSER_STATUS, default='A')
  coupon = models.CharField(max_length=60, null=True)
  counter = models.PositiveIntegerField(max_length=10, default=0)
  cancel_counter = models.PositiveIntegerField(max_length=10, default=0)
  contract = models.BooleanField(default=False)

  class Meta:
    unique_together = ('reseller', 'taxpayer_id')

class ResellerUserInvoice(models.Model):
  reseller = models.ForeignKey('Reseller')
  taxpayer_id = models.CharField(max_length=14)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=1, choices=BILLING_STATUS, default='A')
  counter = models.PositiveIntegerField(max_length=10, default=0)
  cancel_counter = models.PositiveIntegerField(max_length=10, default=0)
  contract = models.BooleanField(default=False)

  class Meta:
    unique_together = ('reseller', 'taxpayer_id')

class ResellerInvoice(models.Model):
  reseller = models.ForeignKey('Reseller')
  uuid = models.CharField(max_length=36, unique=True)
  taxpayer_id = models.CharField(max_length=14)
  date = models.DateTimeField(auto_now_add=True)
  xml = models.TextField()
  #addenda = models.TextField(null=True)
  original_string = models.TextField(default='')
  cfdi_seal = models.TextField(default='')
  status = models.CharField(max_length=1, choices=INVOICE_STATUS, default='S') 
