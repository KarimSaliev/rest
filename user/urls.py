
from django.urls import path


from user.views import login, logout, register, profile, view_basket
app_name = 'user'
urlpatterns = [
    path('login',login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('view_basket', view_basket, name='view_basket')

]