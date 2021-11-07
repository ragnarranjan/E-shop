from django.shortcuts import render ,redirect
from store.models.product import Product
from store. models.category import Category
from django.views import View

 
class Index(View):
    def get(self,request):
        #products = Product.get_all_product()
        products = None
        categories = Category.get_all_category()
        #category_Id = request.GET ['category']
        categoryid = request.GET.get('category')
        if categoryid:
            products = Product.get_all_product_by_categoryid(categoryid) 
        else:
            products = Product.get_all_product()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print(request.session.get('customer_email'))
        return render(request,"index.html",data,)

        

    def post(self,request):
        product = request.POST.get('product')# here product is name coming from html page and this product is product_id coming from html
        remove = request.POST.get('remove')
        print(product)
        cart = request.session.get('cart')
        print(cart,"--------------------------------------------")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            print(cart)

        request.session['cart'] = cart
        print('cart',request.session['cart'])

        return redirect('home')
