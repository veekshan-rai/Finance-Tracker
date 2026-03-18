from django.shortcuts import render, redirect 
from django.views import View
from expenses.forms import RegisterForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Goals
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
            return redirect('home')
        return render(request, 'register.html', {'form':form})
       
class DashBoard(LoginRequiredMixin, View): # Mixin writen first
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
    
class Transactions(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'transaction_form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('home')
        return render(request, 'transaction_form.html', {'form':form})
    
class TransactionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
       trans = Transaction.objects.all()
       return render(request, 'transaction_list.html', {'trans':trans})
    
class GoalCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = GoalForm()
        return render(request, 'goal_form.html', {'form':form})
    
    # def post(self, request, *args, **kwargs):
    #     form = GoalForm(request.POST)
    #     if form.is_valid():
    #         form.save()


    

    
    

    



            
    
  

    




            

    

