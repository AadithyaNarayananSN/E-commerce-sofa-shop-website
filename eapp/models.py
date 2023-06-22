from django.db import models

# Create your models here.


class regmodel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class productmodel(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.FileField(upload_to="eapp/static")
    def __str__(self):
        return self.name
    # desc = models.CharField(max_length=50)


class wishlistmodel(models.Model):
    uid=models.IntegerField()
    pid = models.IntegerField()
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.FileField(upload_to="eapp/static")
    def __str__(self):
        return self.name



class cartmodel(models.Model):
    uid=models.IntegerField()
    pid = models.IntegerField()
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.FileField(upload_to="eapp/static")
    def __str__(self):
        return self.name



# class buymodel(models.Model):
#     name = models.CharField(max_length=25)
#     price = models.IntegerField()
#     quantity = models.IntegerField()
#     def __str__(self):
#         return self.name


class paymentmodel(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    fname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    paymode = models.CharField(max_length=50)

    def __str__(self):
        return self.name
