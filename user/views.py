from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from dishes.models import Basket

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST) # data from request variable
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html',context)
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! You've successfully registered")
            return HttpResponseRedirect(reverse('user:login'))
    else:

        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'user/register.html',context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance = request.user)

    context = {'title': 'Profile', 'form': form, 'baskets': Basket.objects.filter(user=request.user)}
    return render(request, 'user/profile.html', context)
# Create your views here.
def view_basket(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {'title': 'Basket', 'baskets':baskets}
    return render(request, 'dishes/basket.html', context)
