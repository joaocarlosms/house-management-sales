from django.db import models
import uuid

class Owner(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    number_phone = models.CharField(max_length=20, blank=False, null=False)
    cpf = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f'{self.name} - {self.number_phone}'

class TypeConstruction(models.Model):
    type_construction = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.type_construction

class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    number_rooms = models.IntegerField(blank=True, null=True)
    number_bathrooms = models.IntegerField(blank=True, null=True)
    total_area = models.FloatField(blank=True, null=True)
    total_ground = models.FloatField(blank=True, null=True) 
    year_construction = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    owner_house = models.ForeignKey(Owner, on_delete=models.PROTECT, related_name='house_owner')
    amenities_list = models.TextField(blank=True, null=True)
    type_construction = models.ForeignKey(TypeConstruction, on_delete=models.CASCADE, related_name='house_typeConstruction')
    photo = models.ImageField(upload_to='house/', blank=True, null=True)

    def __str__(self):
        return f'{self.type_construction} - {self.address}'
