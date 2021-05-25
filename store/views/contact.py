from django.shortcuts import render, redirect
from django.views import View
from store.models.contact import Contact



class Contactview(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        print(fullname, email, subject)
        c = Contact(fullname=fullname, email=email, subject=subject)
        c.save()
        return redirect('homepage')



