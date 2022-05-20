from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Item
from .forms import CreateNewItem


# Create your views here.
def index(response):
    items = Item.objects.all()
    return render(response, 'index.html', {'items': items})


def create(response):
    if response.method == 'POST':
        item_number = response.POST.get('item_number')
        item_name = response.POST.get('item_name')
        item_count = int(response.POST.get('item_count')
                         ) if response.POST.get('item_count') else 0
        try:
            item = Item(item_number=item_number,
                        item_name=item_name, item_count=item_count)
            item.save()
        except IntegrityError:
            items = Item.objects.all()
            return render(response, 'edit.html', {'items': items})

        return HttpResponseRedirect("/")

    else:
        form = CreateNewItem()
    return render(response, 'index.html', {'form': form})


def delete(response, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("/")


def edit(response, id):
    if response.method == 'POST':
        item_number = response.POST.get('item_number')
        item_name = response.POST.get('item_name')
        item_count = int(response.POST.get('item_count')
                         ) if response.POST.get('item_count') else 0
        item = Item.objects.get(id=id)
        item.item_number, item.item_count, item.item_name = item_number, item_count, item_name
        item.save()
        return HttpResponseRedirect("/")
