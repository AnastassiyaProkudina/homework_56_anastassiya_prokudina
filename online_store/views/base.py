from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from online_store.forms import SearchForm
from online_store.models import Product, CategoryChoice


def products_list(request: WSGIRequest):
    form = SearchForm
    title = request.GET.get("title")
    message = ""
    if title:
        products = (
            Product.objects.all()
            .filter(is_deleted=False, balance__gte=0, title=title)
            .order_by("category", "title")
        )
        if len(products) == 0:
            message = 'Sorry, nothing at here! Try again!'
    else:
        products = (
            Product.objects.all()
            .filter(is_deleted=False, balance__gte=0)
            .order_by("category", "title")
        )
    context = {"products": products, "choices": CategoryChoice.choices, "form": form, "message": message}
    return render(request, "products/index.html", context=context)
