from django.db import models

# Create your models here.
# class ToDoList(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

class Item(models.Model):
    # todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item_number = models.CharField(max_length=200, blank=True, null=False, unique=True)
    item_name = models.CharField(max_length=200)
    item_count = models.IntegerField(default=0)
    # barcode = models.ImageField()
    # complete = models.BooleanField()

    def __str__(self):
        return self.item_name