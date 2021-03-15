from django.db import models


class UnionBoard(models.Model):
    shop_url = models.CharField(primary_key=True, max_length=500)
    url = models.CharField(max_length=200)
    pro_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    delivery_fee = models.CharField(max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'union_board'
        
class OverseeBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oversee_board'
#################################################################################
class FmBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fm_board'
        
        
class PpBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pp_board'        
        
        
class CoolBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cool_board'        
        
class RuliBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruli_board'        
        
#################################################################################
  
class AuctionBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    delivery_fee = models.CharField(max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auction_board'

        
        
class CoupangBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupang_board'        
        
        
class ElevenBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eleven_board'
        
        
class GmarketBoard(models.Model):
    url = models.CharField(primary_key=True, max_length=190)
    shop_url = models.CharField(max_length=190, blank=True, null=True)
    pro_name = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=190, blank=True, null=True)
    delivery_fee = models.CharField(max_length=190, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmarket_board'        
        
        
        
        
        
        
        
        
        
        
        