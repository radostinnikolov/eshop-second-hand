from django.shortcuts import render

from .models import ShopItem


# Create your views here.
def home(request):
    items = ShopItem.objects.all()
    return render(request,"home.html", {"items":items})