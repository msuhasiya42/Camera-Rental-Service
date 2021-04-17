# import databases tables

# Create your views here.
from django.shortcuts import render, redirect

from shop.models.products import Products
from shop.models.category import Category
from shop.models.orders import Order
from django.views import View


class home(View):
    def get(self, request):

        # if there is no cart in session
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        # products = Product.get_all_products()
        # Getting all the categories from the db
        categories = Category.get_all_categories()
        # to get product by category id from the url
        categoryID = request.GET.get('category')

        orders = Order.get_all_orders()

        if categoryID:
            products = Products.get_all_products_by_id(categoryID)
        else:
            products = Products.get_all_products()

        data = {}
        data['categories'] = categories
        data['products'] = products
        # # to get all the orders
        # data['orders'] = orders

        if request.session.get('vendorname'):
            print("you are:", request.session.get('vendorname'))
        else:
            print("You are:",request.session.get('username'))

        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        # item is added to cart and value is set to 1
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    cart[product] = quantity - 1
                # to increase the quantity more than one
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            # if there is no item in the cart
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print(request.session['cart'])
        return redirect('home')
