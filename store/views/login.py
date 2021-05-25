from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_Url = None
    def get(self, request):
        Login.return_Url = request.GET.get('return_Url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_Url:
                    return HttpResponseRedirect(Login.return_Url)
                else:
                    Login.return_Url = None
                    return redirect('homepage')

            else:
                error_message = 'email or Password Invalid..!!'

        else:
            error_message = 'email or Password Invalid..!!'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')