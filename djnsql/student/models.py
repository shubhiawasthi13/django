from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    city=models.CharField(max_length=50)
    

    # def __str__(self):  # use in single register data
    #     # return str(self.id)
    #     return self.name
