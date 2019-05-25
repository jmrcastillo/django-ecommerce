

from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# add cart to the product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    template_name = 'shop/product/list.html'
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  template_name,
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   # add cart to the product
                   'cart_product_form': cart_product_form})


def product_detail_popup(request, id, slug):
    template_name = 'shop/product/product_detail_popup.html'
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  template_name,
                  {"product": product,
                   "cart_product_form": cart_product_form})
