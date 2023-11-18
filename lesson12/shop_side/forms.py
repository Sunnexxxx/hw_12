from django import forms
from django.shortcuts import render, redirect
from shop_side.models import Product, Category


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']


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


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']

