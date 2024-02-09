from django.db import models
import uuid
# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('sandels',"sandels"),
        ('sneakers','sneakers'),
        ('boots','boots'),
        ('formal shoe','formal shoe'),
        ('trainers','trainers'),
        ('slip-ons','slip-ons')
    )
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=11,choices=CATEGORY)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    id = models.UUIDField(default = uuid.uuid4,unique = True, primary_key = True, editable=False)

    def __str__(self):
        return self.name






