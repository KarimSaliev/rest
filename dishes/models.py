from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128, unique=True)
    icon = models.CharField(null=True, max_length=128, unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Dish(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes_images')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(null=True, to=Category, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

class Booking(models.Model):
    def __str__(self):
        return self.full_name
    full_name = models.CharField(max_length=128, unique=False)
    email = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    npeople = models.IntegerField()
    message = models.CharField(max_length=1000, blank=True)

    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'bookings'

class CustomerSupport(models.Model):
    def __str__(self):
        return self.full_name

    full_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    subject = models.CharField(max_length=1000, blank=True)
    message = models.CharField(max_length=1000, blank=True)

    class Meta:
        verbose_name = 'csform'
        verbose_name_plural = 'csforms'


class Employee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128, unique=True)
    position = models.CharField(max_length=128, blank=True)
    image = models.ImageField(null=True, upload_to='employees_images')
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum()for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    dish = models.ForeignKey(to=Dish, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.dish.price*self.quantity

class Order(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=128, blank=True)
    credit_card = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)
    basket = models.CharField(max_length=1000, blank=True)
    total_price = models.IntegerField(max_length=1000,blank=True, null=True)


class Review(models.Model):
    full_name = models.CharField(max_length=128, blank=True)
    profession = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='clients_images')
    review = models.CharField(max_length=128, blank=True)





