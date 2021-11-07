from django.shortcuts import render , redirect
from store.models.customer import Customer 
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            phone = phone,
                            email = email,
                            password = password)
        value = {
                'first_name' : first_name,
                'last_name' : last_name,
                'phone' : phone,
                'email' : email
            }
        
        error_msg = self.validateCustomer(customer)
        
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register() 
            print(customer)
            return redirect('home')
        else:
            data = {
                'error' : error_msg,
                'values' : value
            }
            return render(request, 'signup.html',data)  # here error is coming from html we r making dict to obtain specific error msg 


    def validateCustomer(self,customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():  ## here isexists is not @static method so we rr not calling it with clas name Customer.isexists
            error_message = 'Email Address Already Registered..'
        # saving
    
        return error_message

   