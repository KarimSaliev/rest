from django import forms
from dishes.models import Booking, CustomerSupport, Order

class BookingForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Your Name',

    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', "placeholder": 'Your Email'
    }))
    date = forms.CharField(widget=forms.DateTimeInput(attrs={
        'class': 'form-control datetimepicker-input', "placeholder": 'Data & Time',
        'data-target': '#date3',
        'data-toggle': 'datetimepicker'
    }))
    npeople = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Number of People'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', "placeholder": 'Special Request',

    }))

    class Meta:
        model = Booking
        fields = ('full_name', 'email', 'date', 'npeople', 'message')

class CustomerSupportForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Your Name',

    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', "placeholder": 'Your Email'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', "placeholder": 'Leave a message here',
    }))

    class Meta:
        model = CustomerSupport
        fields = ('full_name', 'email', 'subject', 'message')

class OrderForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'First Name',

    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Last Name',

    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', "placeholder": 'Your Email'
    }))

    credit_card = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Credit Card Number'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "placeholder": 'Your Address'
    }))
    user = forms.CharField(widget=forms.HiddenInput(attrs={
        'class': 'form-control', "placeholder": 'User',


    }))
    basket = forms.CharField(widget=forms.HiddenInput(attrs={
        'class': 'form-control', "placeholder": 'Basket',

    }))
    total_price = forms.IntegerField(widget=forms.HiddenInput(attrs={
        'class': 'form-control', "placeholder": 'Total Price'
    }))


    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'credit_card', 'address', 'user', 'basket','total_price')



