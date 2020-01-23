from django.db import models

# Create your models here.
class Offer(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    original_price = models.IntegerField(default=0)
    offer_price=models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/menucard', default="")
    def __str__(self):
        return self.product_name
class Specials(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    original_price = models.IntegerField(default=0)
    offer_price=models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/menucard', default="")
    def __str__(self):
        return self.product_name