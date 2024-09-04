from django.shortcuts import render


def catalog(request):
    context = {
        "tiitle": "Home - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Прикроватный столик",
                "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
                "price": 25.00,
            },
        ],
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
