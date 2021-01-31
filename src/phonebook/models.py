from django.db import models

# Create your models here.

class Persone(models.Model):
    name = models.CharField("Contact", max_length=50)

    def __str__(self):
        return self.name

class Phone(models.Model):
    phone = models.CharField('Number', max_length=50)
    contact = models.ForeignKey(Persone, on_delete=models.CASCADE, related_name="phones")

    def __str__(self):
        return self.phone
