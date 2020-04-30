from django.db import models

# Create your models here.


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone= models.CharField(max_length=20)
    username= models.CharField(max_length=20,primary_key=True)
    pswd= models.CharField(max_length=20)
    #username= models.PrimaryKey(Position,on_delete=models.CASCADE)
    #pswd = models.ForeignKey(Position,on_delete=models.CASCADE)

   #position = models.ForeignKey(Position,on_delete=models.CASCADE)
    
def __str__(self):
    return self.name