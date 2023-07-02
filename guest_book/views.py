from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest_book
from .forms import GuestForms, SearchForm
# Create your views here.

def home(request):
    form = SearchForm()
    guest = Guest_book.objects.filter(status='active').order_by('-time_of_creation')

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            guest = guest.filter(name=name)
        return render(request, 'home.html', context={'guest': guest, 'form': form})
    else:
        return render(request, 'home.html', context={'guest': guest, 'form': form})



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
