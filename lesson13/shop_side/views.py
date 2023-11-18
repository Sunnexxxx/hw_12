from django.shortcuts import render, redirect
from shop_side.models import Product, Category
from .forms import ProductCreateForm
from .forms import ProductUpdateForm


def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    if request.method == 'POST':
        form = ProductCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductCreateForm()

    context['form'] = form
    return render(request, 'shop_side/product_create.html', context)


def product_delete_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product.delete()

    return redirect('product_list')


def product_update_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == "POST":
        form = ProductUpdateForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductUpdateForm(instance=product)

    context = {
        'form': form,
        'category_list': Category.objects.all()
    }
    return render(request, 'shop_side/product_update.html', context)









