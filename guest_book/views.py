from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest_book
from .forms import GuestForms
# Create your views here.

def home(request):
    guest = Guest_book.objects.filter(status='active').order_by('-time_of_creation')
    return render(request, 'home.html', context={'guest': guest})


def add_guest(request):
    if request.method == 'POST':
        print(request.POST)
        form = GuestForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GuestForms
    return render(request, 'add_guest.html', {'form': form})


def edit_guest(request, id):
    guest = get_object_or_404(Guest_book, id=id)
    if request.method == 'GET':
        form = GuestForms(instance=guest)
        return render(request, 'edit_guest.html', {'guest': guest, 'form': form})
    elif request.method == 'POST':
        form = GuestForms(data=request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'edit_guest.html', {'guest': guest, 'form': form})


def delete_guest(request, id):
    guest = get_object_or_404(Guest_book, id=id)
    guest.delete()
    return redirect('home')
