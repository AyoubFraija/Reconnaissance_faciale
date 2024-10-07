from django.db import models

# Create your models here.
class Presence(models.Model):
    username= models.CharField(max_length=150)
    date=models.DateTimeField(6)
    present= models.CharField(default="Non détecté(e)",max_length=150)
    class Meta :
        db_table='presence'