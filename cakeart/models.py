from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone
from uuid import uuid4
from uuid import UUID
import uuid
# from django_extensions.db.Fields import UUIDField


# Create your models here.
class User_type(models.Model):
    utname=models.CharField(max_length=30)


class User(models.Model):
    utid=models.ForeignKey(User_type,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    DOB=models.DateField()
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    pinc=models.IntegerField()
    License=models.FileField(upload_to='file/',default='')
    shopnm=models.CharField(max_length=30,null=True,default='',blank=True)
    email=models.CharField(max_length=30)
    pwd=models.CharField(max_length=10)
    otp=models.IntegerField(blank=True,null=True)

class Category(models.Model):
    category_name=models.CharField(max_length=30)
    category_img=models.ImageField(upload_to='image/',default='abc.jpg')

class Package(models.Model):
    package_name=models.CharField(max_length=30)
    package_price=models.IntegerField(blank=True,null=True)
    package_validity=models.CharField(max_length=30)
    package_discount=models.IntegerField(blank=True,null=True)
    package_description=models.CharField(max_length=100)

class Theme(models.Model):
    theme_name=models.CharField(max_length=30,default="GENERAL")

class Flavour(models.Model):
    flavour_name=models.CharField(max_length=30)

class Decoration(models.Model):
    decoration_name=models.CharField(max_length=30)

class Shape(models.Model):
    shape_name=models.CharField(max_length=30)

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField(blank=True,null=True)
    product_type=models.CharField(max_length=20)
    product_desc=models.CharField(max_length=500)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='image/',default='')
    theme_id=models.ForeignKey(Theme,on_delete=models.CASCADE)
    decoration_id=models.ForeignKey(Decoration,on_delete=models.CASCADE)
    shape_id=models.ForeignKey(Shape,on_delete=models.CASCADE)
    flavor_id=models.ForeignKey(Flavour,on_delete=models.CASCADE,null=True,blank=True)
    # qnty=models.IntegerField(default=5,null=True,blank=True)

class Feedback(models.Model):
    feedback_abt=models.CharField(max_length=20,null=True,default='')
    feedback_text=models.CharField(max_length=500)
    feedback_date=models.DateTimeField(default=timezone.now,blank=True,null=True)
    to_vb=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    # from_cust=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

#-------------------Vendor's Model---------------------------

class Cart(models.Model):
    prodid=models.ForeignKey(Product,on_delete=models.CASCADE)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    qnty=models.IntegerField(default=1)
    rowtotal=models.FloatField(default=0.0)
    cnm=models.CharField(max_length=100,default='')


class Products(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField(blank=True,null=True)
    product_type=models.CharField(max_length=20)
    product_desc=models.CharField(max_length=500)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='image/',default='')
    theme_id=models.ForeignKey(Theme,on_delete=models.CASCADE)
    decoration_id=models.ForeignKey(Decoration,on_delete=models.CASCADE)
    shape_id=models.ForeignKey(Shape,on_delete=models.CASCADE)
    flavor_id=models.ForeignKey(Flavour,on_delete=models.CASCADE,null=True,blank=True)
    qty=models.IntegerField(default=5)
    # qnty=models.IntegerField(default=5,null=True,blank=True)

class OrderMaster(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    BillingAddress=models.CharField(max_length=130)
    order_dt=models.DateField(default=date.today,blank=True,null=True)
    TotalPrice=models.FloatField(null=True,blank=True)

class OrderDetailing(models.Model):
    orderid=models.ForeignKey(OrderMaster,on_delete=models.CASCADE)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    prodid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    prc=models.FloatField(default=0.0)
    cnm=models.CharField(max_length=50,default='')
    dt=models.DateField(default=date.today,blank=True,null=True)

class Payment(models.Model):
    txid=models.CharField(max_length=50,default='')
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    omid=models.ForeignKey(OrderMaster,on_delete=models.CASCADE)


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=1000, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)