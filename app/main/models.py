from django.db import models

# Create your models here.


class Item(models.Model):
    item_number = models.CharField(
        max_length=200, blank=True, null=False, unique=True)
    item_name = models.CharField(max_length=200)
    item_count = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name
