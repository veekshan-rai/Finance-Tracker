from django.shortcuts import render, redirect 
from django.views import View
from expenses.forms import RegisterForm
from django.contrib.auth import login
#Function Based View

# def home(request):
#     return HttpResponse("Hello Django")

#  Class Based View:
#  class HomeView(View):
#     def get(sef, request, *args, **kwargs):
#          return HttpResponse("<h2>Hello This is Class house</h2>")

# class HomeView(View):
#     def get(sef, request, *args, **kwargs):
#         return render(request, 'home.html')

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form}) #context
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('register')
        return render(request, 'register.html', {'form': form})
            

    

