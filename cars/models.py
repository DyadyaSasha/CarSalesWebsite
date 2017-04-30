from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Acount(models.Model):
#     login = models.CharField(unique=True, max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.EmailField(max_length=50)
#     name = models.CharField(max_length=16)
#     lastname = models.CharField(max_length=16)
#     registration_date = models.DateTimeField(auto_now_add=True)
#     user = models.OneToOneField(User)
    
    # def __str__(self):
    #     return self.name
    # class Meta:
    #     db_table = 'acount'
    #     ordering = ['registration_date']

# class Session(models.Model):
#     key = models.CharField(unique=True, max_length=20)
#     user = models.ForeignKey(Acount)
#     espire = models.DateTimeField()
    
    # def __str__(self):
    #     return self.key

    # class Meta:
    #     db_table = 'session'
    #     ordering = ['user']

class Car(models.Model):
    firm = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    type_of_transmission = models.BooleanField() #true - auto, false - mechanics
    image = models.ImageField(null=True, upload_to ="images/")#????
    status = models.BooleanField(default=True) #true - free, false - overwise
    price = models.IntegerField()
    
    def __str__(self):
        return self.model

    class Meta:
        db_table = 'car'
        ordering = ['price']

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    acount = models.ForeignKey(User)
    car = models.ForeignKey(Car)
    
    def __str__(self):
        return self.order_date

    class Meta:
        db_table = 'order'
        ordering = ['amount']


