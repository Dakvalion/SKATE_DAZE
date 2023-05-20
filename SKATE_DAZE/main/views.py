
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from .forms import *


# Create your views here.
def SD(request):
    error = ''
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "No"

    form = MailForm()
    return render(request, 'main/SD.html', {'title': 'SKATE DAZE', 'form': form, 'error': error})


def LogIn(request):
    return render(request, 'main/LogIn.html', {'title': 'Вход в аккаунт'})


def SignIn(request):
    error = ''
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "No"

    form = RegForm()

    return render(request, 'main/reg.html', {'title': 'Регистрация', 'form': form, 'error': error})


def Catalog(request):
    products = Items.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/Catalog.html', {'page_obj': page_obj, 'title': 'Каталог', 'products': products})


def account(request):
    if request.user.is_superuser:  # just using request.user attributes
        accounts = get_user_model().objects.all()
