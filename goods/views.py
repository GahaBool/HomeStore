from django.shortcuts import render

from goods.models import Categories, Products


def catalog(request):

    goods = Products.objects.all()
    categories = Categories.objects.all()

    context = {
        "tiitle": "Home - Каталог",
        "goods": goods,
        "categories": categories,
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
