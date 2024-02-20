from django.contrib import admin
from dishes.models import Dish, Category, Employee, Basket, Order, CustomerSupport, Booking, Review
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'category', 'description',)
    fields = ('name','price','image', 'category', 'description',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','icon')
    fields = ('name','icon')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Employee)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','position','image')
    fields = ('name','position','image')
    search_fields = ('name',)
    ordering = ('name',)
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'dish', 'quantity','create_timestamp',)
    extra = 0

@admin.register(Order)
class BasketAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name', 'last_name', 'email', 'credit_card', 'address', 'user','basket', 'total_price')


@admin.register(CustomerSupport)
class CustomerSupportAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name','email','subject','message')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name', 'email', 'date', 'npeople', 'message')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'image', 'review')
    fields = ('full_name', 'profession', 'image', 'review')
    search_fields = ('full_name',)
    ordering = ('full_name',)
