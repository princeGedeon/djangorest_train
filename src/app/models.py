from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    content=models.TextField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    @property
    def discount(self):
        return float(self.price)*0.5