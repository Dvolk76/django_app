from django.db import models

# Create your models here.

class City(models.Model):
    
    name = models.CharField(
        verbose_name="City's name",
        max_length=20)
    description = models.TextField(
        verbose_name="City's description",
        null=True,
        blank=True)
    created = models.DateTimeField(
        verbose_name="Created date time",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Updated date time",
        auto_now=True,
        auto_now_add=False
    )
    def __str__(self):
        return self.name

class Address(models.Model):
    city = models.ForeignKey(
        'phonebook.City',
        verbose_name="City",
        on_delete=models.PROTECT,
        related_name="addresses"
    )
    street = models.CharField(
        verbose_name="Street name",
        max_length=80
    )
    building_number = models.PositiveIntegerField(
        verbose_name="building number"
    )
    block = models.CharField(
        verbose_name="Block",
        null=True,
        blank=True,
        max_length=3
    )

    def __str__(self):
        return f'{self.city.name} {self.street} {self.building_number} {self.block}'


    