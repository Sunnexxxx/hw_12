from django.shortcuts import render, redirect
from .models import Product, Category
from .validator import validate_name, validate_price, validate_quantity


def product_create_view(request):
    context = {'category_list': Category.objects.all()}
    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        if not all([name, price, quantity, category]):
            error_message = 'Все поля должны быть заполнены'
        else:
            try:
                validate_name(name)
                validate_price(price)
                validate_quantity(quantity)

                category_obj = Category.objects.get(pk=category)
                product = Product.objects.create(name=name, price=float(price), quantity=int(quantity), category=category_obj)
                return redirect('product_list')

            except ValueError as e:
                error_message = str(e)
            except Category.DoesNotExist:
                error_message = 'Выбранная категория не существует.'

    context['error_message'] = error_message
    return render(request, 'shop_side/product_create.html', context)
