from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phonenumber')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required..!!"
        elif (not customer.last_name):
            error_message = "Last Name Required..!!"
        elif len(customer.last_name) < 3:
            error_message = "Last Name Must be 3 Char long"
        elif not customer.phone:
            error_message = 'Phone Number Required'
        elif len(customer.phone) < 11:
            error_message = 'Phone Number Must be 11 Char Long'
        elif len(customer.email) < 16:
            error_message = 'Email Must be 16 char Long'
        elif len(customer.password) < 8:
            error_message = 'Password Must be 8 Digit Long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered'
        return error_message
