from django.db import models

# Create your models here.
class Booking(models.Model):
    
    restaurantname = models.TextField()
    bookname = models.TextField()
    bookperson = models.PositiveIntegerField()
    booktel= models.TextField()
    bookdate= models.TextField()
    bookwhen = models.TextField()
    booktime = models.TextField()
    
    class Meta:
        db_table = "book"
class Restaurant(models.Model):
    rname = models.TextField()
    rtype = models.TextField()
    rtel= models.TextField()
    raddress = models.DateField()
    rweb= models.TextField()
    rintroduction= models.TextField(max_length=500)
    
    class Meta:
        db_table = "restaurants"