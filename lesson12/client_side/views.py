from django.shortcuts import render
from shop_side.models import Product


def product_list_view(request):
    context = {'product_list': Product.objects.all()}
    return render(request,
                  'client_side/product_list.html',
                  context)


def product_detail_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request,
                  'client_side/product_detail.html',
                  context)




