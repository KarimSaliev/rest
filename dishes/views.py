from django.shortcuts import render
from dishes.models import Dish, Booking, Category, CustomerSupport, Employee, Basket, Order, Review
from django.http import HttpResponseRedirect
from dishes.forms import BookingForm, CustomerSupportForm, OrderForm
from django.contrib.auth.decorators import login_required

def index(request, category_id=None):

    dishes = Dish.objects.all()
    if category_id:
        dishes = dishes.filter(category_id=category_id)
    categories = Category.objects.all()
    team = Employee.objects.all()
    reviews = Review.objects.all()
    context = {'title': 'Restaurant',
               'form': BookingForm(), 'dishes': dishes, 'categories': categories, 'cat_id':category_id, 'team':team,'reviews':reviews}
    return render(request, 'dishes/index.html',context)
# Create your views here.

def menu(request, category_id=None):
    dishes = Dish.objects.all()
    if category_id:
        dishes = dishes.filter(category_id=category_id)
    categories = Category.objects.all()

    context = {'title': 'Menu',
               'dishes':dishes, 'categories': categories, 'cat_id':category_id}
    return render(request, 'dishes/menu.html', context)

def book_table(request):
    if request.method=='POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            email = request.POST['email']
            date = request.POST['date']
            npeople = request.POST['npeople']
            message = request.POST['message']
            booking = Booking(full_name=full_name, email=email,
                                  date=date, npeople=npeople, message=message)
            booking.save()
            request.session['booking_data']={'full_name': booking.full_name, 'email': booking.email, 'date':booking.date, 'npeople': booking.npeople, 'message': booking.message}
            return HttpResponseRedirect('booking_thanks')
    else:
        form = BookingForm()
    context = {'form':form}
    return render(request, 'dishes/booking.html', context)



def about(request):
    team = Employee.objects.all()
    context = {'title': 'About', 'team': team}
    return render(request, 'dishes/about.html', context)

def service(request):
    context = {'title':'Service'}
    return render(request, 'dishes/service.html', context)



def contact(request):
    if request.method=='POST':
        form =CustomerSupportForm(data=request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            cscontact = CustomerSupport(full_name=full_name, email=email, subject=subject, message=message)
            cscontact.save()
            request.session['data']={'full_name': cscontact.full_name,
                                     'email': cscontact.email,
                                     'subject': cscontact.subject,
                                     'message':cscontact.message}
            return HttpResponseRedirect('cs_thanks')
    else:
        form = CustomerSupportForm()
    context = {'form':form}
    return render(request, 'dishes/contact.html', context)


def team(request):
    employees = Employee.objects.all()
    context = {'title': 'Team', 'team':employees}
    return render(request, 'dishes/team.html', context)
@login_required
def basket_add(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    baskets = Basket.objects.filter(user=request.user, dish=dish)

    if not baskets.exists():
        Basket.objects.create(user=request.user, dish=dish, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity +=1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def purchase(request):
    user = request.user
    basket = Basket.objects.filter(user=request.user)
    string = ""
    total_sum = 0

    for b in basket:
        string += f"{b.quantity} {b.dish.name} (s)\n"
        total_sum += b.sum()
    if request.method=='POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            credit_card = request.POST['credit_card']
            address = request.POST['address']
            order = Order(first_name=first_name,
                          last_name=last_name,
                          email=email, credit_card=credit_card,
                          address=address, user=user, basket = string,total_price=total_sum)


            order.save()
            return HttpResponseRedirect('thanks')
    else:
        form = OrderForm(initial={'user':user, 'basket':basket, 'total_price':total_sum})

    basket = Basket.objects.filter(user=request.user)

    context = {'title': 'Checkout', 'form':form, 'basket':basket}
    return render(request, 'dishes/order.html',context)

def thankYou(request):
    basket = Basket.objects.filter(user=request.user)
    context = {'title': 'Thank You!', 'basket': basket}
    return render(request, 'dishes/thanks.html', context)

def cs_thanks(request):
    data = request.session['data']
    context = {'title': 'Customer Support', 'message': data}
    return render(request, 'dishes/cs_thanks.html', context)

def testimonial(request):
    reviews = Review.objects.all()
    context = {'title': 'Testimonial', 'reviews': reviews}
    return render(request, 'dishes/testimonial.html', context)

def booking_thanks(request):
    data = request.session['booking_data']
    context = {'title':'Booking', 'message': data}
    return render(request, 'dishes/booking_thanks.html', context)




