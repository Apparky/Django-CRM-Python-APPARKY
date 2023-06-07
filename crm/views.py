from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import *


# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django')


def home(request):
    datas = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have been Logged in')
            return redirect('home')

        else:
            messages.success(request, 'Login Error...!! Please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'datas': datas})


def log_out(request):
    logout(request)
    messages.success(request, "You have been Successfully Logged out")
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully done the Registration')
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def records(request, pk):
    if request.user.is_authenticated:
        cst_records = Record.objects.get(id=pk)
        return render(request, 'records.html', {'records': cst_records})

    else:
        messages.error(request, 'Something went Wrong...!')
        return redirect('home')


def delete_cst(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()

        messages.success(request, 'Records has been deleted Successfully')
        return redirect('home')

    else:
        messages.error(request, 'Something went Wrong..!!')
        return redirect('home')


def add_cst(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            add = form.save()
            messages.success(request, 'Record has been Updated')
            return redirect('home')
        return render(request, 'add.html', {'form': form})

    else:
        messages.error(request, 'Something Went Wrong....!')
        return redirect('home')


def update_cst(request, pk):
    if request.user.is_authenticated:
        the_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=the_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update.html', {'form': form})

    else:
        messages.error(request, 'Something went Wrong....!!')
        return redirect('home')



