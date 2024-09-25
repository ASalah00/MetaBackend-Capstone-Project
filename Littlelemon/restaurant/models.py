from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    booking_date=models.DateField()
    def __str__(self) -> str:
        return self.name
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'