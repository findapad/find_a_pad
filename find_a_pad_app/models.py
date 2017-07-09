from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __repr__(self):
        return "{}".format(self.name)


class Organization(models.Model):
     name = models.CharField(max_length=200)
     address = models.CharField(max_length = 1000)
     phone_number = models.CharField(max_length=12)
     email = models.CharField(max_length=100)
     type = models.ForeignKey(Type, on_delete=models.CASCADE)

     def __repr__(self):
         return "{}".format(self.name)












