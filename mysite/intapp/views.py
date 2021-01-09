from django.shortcuts import render, redirect
from .models import Name, Arti
from .forms import NameForm, ArtiForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib import messages

# Create your views here.

def userx(request):
    intapp = Arti.objects.all()
    return render(request, 'intapp/index.html', {'intapp': intapp})

class news_detail(DetailView):
    model = Arti
    template_name = 'intapp/detail_view.html'
    context_object_name = 'Artic'

class news_update(UpdateView):
    model = Arti
    template_name = 'intapp/create.html'
    form_class = ArtiForm
    # fields = ['title', 'pasword', 'full_text', 'date']


def creat(request):
    error = ''
    if request.method == 'POST':
        form = ArtiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была не верной"
    form = ArtiForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'intapp/create.html', data)


class Delete(DeleteView):
    model = Arti
    success_url = '/intapp/'
    template_name = 'intapp/Delete.html'

def index(request):
    return render(request, 'intapp/index.html')


def xnx(request):
    intapp = Name.objects.all()
    return render(request, 'intapp/in.html', {'intapp': intapp})


def user_login(request):
    return render(request,'logout')

def us_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # после входы возврашает на главную страницу
        # return redirect('users')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'intapp/login.html', context)


def logoutUsers(request):
    logout(request)
    return redirect('login')


def us_regis(request):
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            # после регистрации переходит на страницу входа
            return redirect('us_login')

    context = {'form': form}
    return render(request, 'intapp/register.html', context)


def regi(request):
    error = ''
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regis')
        else:
            error = "Форма была не верной"

    form = NameForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'intapp/registr.html', data)


