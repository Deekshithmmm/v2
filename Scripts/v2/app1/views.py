from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def show(request):
    data = Item.objects.all()
    return render(request, "show.html", {"data": data})


def add(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add")
    else:
        form = ItemForm()

    return render(request, "add.html", {"form": form})
