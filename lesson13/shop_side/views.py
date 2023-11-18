from django.shortcuts import render, redirect
from shop_side.models import Product, Category


def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        if not (name and price and quantity and category):
            context['error_message'] = 'Все поля должны быть заполнены!'
        else:
            try:
                price = float(price)
                quantity = int(quantity)
                category_obj = Category.objects.get(pk=category)

                product = Product()
                product.name = name
                product.price = price
                product.quantity = quantity
                product.category = category_obj
                product.save()

                return redirect('product_list')

            except ValueError:
                context['error_message'] = 'Цена и количество должны быть числами!'
            except Category.DoesNotExist:
                context['error_message'] = 'Выбранная категория не существует!'

    return render(request, 'shop_side/product_create.html', context)



