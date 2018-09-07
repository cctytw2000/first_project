from django.db import models

# Create your models here.
class Restaurant(models.Model):
    rname = models.TextField()
    rtype = models.TextField()
    rtel= models.TextField()
    raddress = models.DateField()
    rweb= models.TextField()
    rintroduction= models.TextField(max_length=500)
    
    class Meta:
        db_table = "restaurants"