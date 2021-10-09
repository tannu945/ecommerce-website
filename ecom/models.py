from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price_product=models.IntegerField(default=0)
    desc=models.CharField(max_length=3000)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="ecom/images",default="")

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    contact_name=models.CharField(max_length=50, default="")
    contact_email=models.CharField(max_length=50, default="")
    contact_phone=models.CharField(max_length=50, default="")
    contact_desc=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.contact_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5200)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "...."
