from django.urls import path
from dishes.views import index,book_table, about, menu, service,contact, team,\
    basket_add, basket_remove, purchase, thankYou, cs_thanks, testimonial, booking_thanks
app_name = 'dishes'
urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', index, name='category'),
    path('booktable', book_table, name = 'book_table'),
    path('menu', menu, name='menu'),
    path('menu/category/<int:category_id>/', menu, name='m_category'),
    path('about', about, name = 'about'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('team', team, name='team'),
    path('basket/add/<int:dish_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('order', purchase, name='order'),
    path('thanks', thankYou, name='thanks'),
    path('cs_thanks', cs_thanks, name='cs_thanks'),
    path('testimonial', testimonial, name='testimonial'),
    path('booking_thanks', booking_thanks, name='booking_thanks')


    ]