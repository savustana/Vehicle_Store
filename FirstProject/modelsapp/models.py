from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Filter(models.Manager):
    sorted = True

    def get_first_by_id(self, id_car):
        return self.filter(pk=id_car).first()

    def get_all(self):
        return self.all()

    def filter_year_max(self):
        self.sorted = not self.sorted
        return self.all().order_by('year')

    def filter_year_min(self):
        self.sorted = not self.sorted
        return self.all().order_by('-year')

    def filter_price_max(self):
        self.sorted = not self.sorted
        return self.all().order_by('price')

    def filter_price_min(self):
        self.sorted = not self.sorted
        return self.all().order_by('-price')

    def filter_custom_price(self, min_price=0, max_price=1000000):
        self.sorted = not self.sorted
        return self.all().filter(price__gte=min_price, price__lte=max_price)

    def filter_search(self, search):
        if self.filter(description__icontains=search):
            return self.filter(description__icontains=search)
        return self.all()


class Car(models.Model):
    Brand_Choices = (
        ('Audi', "Audi"),
    )

    Transmission_Choices = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )
    objects = Filter()
    brand = models.CharField(max_length=50, choices=Brand_Choices)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    year = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    engine = models.CharField(max_length=50, null=True, blank=True)
    fuel_system = models.CharField(max_length=50, null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    transmission = models.CharField(max_length=50, choices=Transmission_Choices, null=True, blank=True)
    rate = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)


class Motorcycle(models.Model):
    objects = Filter()
    Brand_Choices = (
        ('Kawasaki', 'Kawasaki'),
    )

    brand = models.CharField(max_length=50, choices=Brand_Choices)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    year = models.IntegerField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    engine = models.CharField(max_length=50, null=True, blank=True)
    fuel_system = models.CharField(max_length=50, null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    rate = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)

    def clean(self):
        if self.price < 1000:
            raise ValidationError('Price must be greater than 1000')
