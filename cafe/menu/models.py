from django.db import models

# Create your models here.
class Menu(models.Model):
    # product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(primary_key=True,max_length=50)
    category = models.CharField(max_length=50, default="")
    original_price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/menucard', default="")
    def __str__(self):
        return self.product_name
class FeedBack(models.Model):
    product_name = models.CharField(max_length=50)
    product_ratings=models.IntegerField(default=2.5)
    comment = models.CharField(max_length=200)
    def __str__(self):
        return self.product_name




