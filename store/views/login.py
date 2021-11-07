from django.views import View
from django.shortcuts import render , redirect
from store.models.customer import Customer 
from django.contrib.auth.hashers import check_password


class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        #import ipdb;
        #ipdb.set_trace()
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                print("11111111111111111111111111111111")
                print("000000000000000000000000000000000")
                return redirect('home')
                
            else:
                print("666666666666666666666666666666")
                error_message = 'Email or Password invalid !!'
        else:
                error_message = 'Email or Password invalid !!'
                print("000000000000000000000000000000")
        print(email, password)
        return render(request, 'login.html', {'error': error_message})





# from django.shortcuts import render , redirect
# from .models.product import Product
# from . models.category import Category
# #from .models.customer import Customer 
# #from django.http import HttpResponse
# #from django.contrib.auth.hashers import make_password,check_password
# #from django.views import View

# def index(request):
#     #products = Product.get_all_product()
#     products = None
#     categories = Category.get_all_category()
#     #category_Id = request.GET ['category']
#     categoryid = request.GET.get('category')
#     if categoryid:
#         products = Product.get_all_product_by_categoryid(categoryid) 
#     else:
#         products = Product.get_all_product()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     return render(request,"index.html",data)


# def validateCustomer(customer):
#         error_message = None;
#         if (not customer.first_name):
#             error_message = "First Name Required !!"
#         elif len(customer.first_name) < 4:
#             error_message = 'First Name must be 4 char long or more'
#         elif not customer.last_name:
#             error_message = 'Last Name Required'
#         elif len(customer.last_name) < 4:
#             error_message = 'Last Name must be 4 char long or more'
#         elif not customer.phone:
#             error_message = 'Phone Number required'
#         elif len(customer.phone) < 10:
#             error_message = 'Phone Number must be 10 char Long'
#         elif len(customer.password) < 6:
#             error_message = 'Password must be 6 char long'
#         elif len(customer.email) < 5:
#             error_message = 'Email must be 5 char long'
#         elif customer.isExists():  ## here isexists is not @static method so we rr not calling it with clas name Customer.isexists
#             error_message = 'Email Address Already Registered..'
#         # saving

    
#         return error_message



# def registerUser(request): # as we r dealing with Postrequest so have to pass request as a paramtr here  
#     postdata = request.POST
#     first_name = postdata.get('firstname')
#     last_name = postdata.get('lastname')
#     phone = postdata.get('phone')
#     email = postdata.get('email')
#     password = postdata.get('password')
#     customer = Customer(first_name = first_name,
#                         last_name = last_name,
#                         phone = phone,
#                         email = email,
#                         password = password)
#     value = {
#             'first_name' : first_name,
#             'last_name' : last_name,
#             'phone' : phone,
#             'email' : email
#         }
    
#     error_msg = validateCustomer(customer)
    
#     if not error_msg:
#         customer.password = make_password(customer.password)
#         customer.register() 
#         print(customer)
#         return redirect('homepage')
#     else:
#         data = {
#             'error' : error_msg,
#             'values' : value
#         }
#         return render(request, 'signup.html',data)  # here error is coming from html we r making dict to obtain specific error msg 



# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)



# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 print("11111111111111111111111111111111")
#                 return redirect('homepage')
                
#             else:
#                 print("666666666666666666666666666666")
#                 error_message = 'Email or Password invalid !!'
#         else:
#                 error_message = 'Email or Password invalid !!'
#                 print("000000000000000000000000000000")
#         print(email, password)
#         return render(request, 'login.html', {'error': error_message})



        