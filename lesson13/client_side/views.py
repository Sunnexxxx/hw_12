from django.shortcuts import render, redirect

from client_side.models import Comment
from shop_side.models import Product, Category


def product_list_view(request):
    selected_category = request.GET.get('category')
    categories = Category.objects.all()
    products = Product.objects.all()

    if selected_category:
        products = products.filter(category__name=selected_category)

    context = {
        'product_list': products,
        'category_list': categories,
        'selected_category': selected_category
    }

    return render(request, 'client_side/product_list.html', context)


def product_detail_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'comment_list': Comment.objects.filter(product=product)
    }
    return render(request,
                  'client_side/product_detail.html',
                  context)


def comment_create_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')

        comment = Comment()
        comment.product = product
        comment.username = username
        comment.body = body

        comment.save()
        print('Test')

    return redirect('product_detail', product.slug)
