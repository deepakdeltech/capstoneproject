from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    num_guests = models.SmallIntegerField()
    booking_date = models.DateField()
    
    def __str__(self) -> str:
        return self.name
    
    
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return self.title
    
    def get_item(self):
        return f'{self.title}: {str(self.price)}'