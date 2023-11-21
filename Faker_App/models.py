
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    salary = models.IntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table='employee'






