from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def default(request):
    items = Item.objects.all()
    return render(request, "main.html", {"items": items})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("default")
    else:
        form = ItemForm()

    return render(request, "add_item.html", {"form": form})

def item_detail(request, item_name):
    item = get_object_or_404(Item, name=item_name)
    return render(request, "item_detail.html", {"item": item})

def buy_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Item, id=item_id)

        if item.stock > 0:
            item.stock -= 1
            item.save()

    return redirect("default")