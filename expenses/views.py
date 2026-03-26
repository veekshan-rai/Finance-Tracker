from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from expenses.forms import RegisterForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Goals
from django.db.models import Sum
from .admin import TransactionResource
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.urls import reverse_lazy
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
            messages.success(request, 'Account created succsessfully!')
            return redirect('home')
        return render(request, 'register.html', {'form':form})
       
class DashBoard(LoginRequiredMixin, View): # Mixin writen first
    def get(self, request, *args, **kwargs):
        trans = Transaction.objects.filter(user = request.user)
        goals = Goals.objects.filter(user = request.user)

        # Calculate Income and Expenses
        total_income = Transaction.objects.filter(user = request.user, transaction_type = 'Income').aggregate(Sum('amount'))['amount__sum'] or 0

        total_expenses = Transaction.objects.filter(user = request.user, transaction_type = 'Expense').aggregate(Sum('amount'))['amount__sum'] or 0
        
        savings = total_income - total_expenses
        if savings > 0:
            net_saving = savings
        else:
            net_saving = 0
        
        
        remaining_saving = net_saving
        goal_progress = []
        for goal in goals:
            if remaining_saving >= goal.target_amount:
                goal_progress.append({'goal': goal, 'progress': 100})
                remaining_saving -= goal.target_amount
            elif remaining_saving > 0:
                progress = (remaining_saving / goal.target_amount) * 100
                goal_progress.append({'goal': goal, 'progress': progress})
                remaining_saving = 0
            else:
                goal_progress.append({'goal': goal, 'progress': 0})

        context = {
            'trans': trans,
             'total_income': total_income,
             'total_expenses': total_expenses,
             'net_saving': net_saving,
             'goal_progress': goal_progress,
        }
        return render(request, 'home.html', context)
    
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
            messages.success(request, 'Transaction added successfully!')
            return redirect('home')
        return render(request, 'transaction_form.html', {'form':form})
    
class TransactionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
       trans = Transaction.objects.filter(user = request.user)
       return render(request, 'transaction_list.html', {'trans':trans})
    
class GoalCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = GoalForm()
        return render(request, 'goal_form.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal added successfully!')
            return redirect('home')
        return render(request, 'goal_form.html', {'form':form})
    

def export_transactions(request):
    user_transactions = Transaction.objects.filter(user = request.user)
    
    transaction_resource = TransactionResource()
    dataSet = transaction_resource.export(queryset=user_transactions)

    excel_data = dataSet.export('xlsx')

    # create  an HTTP Response with the correct MIME type for excel file 
    response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # set the header for downloading the file 
    response['Content-Disposition'] = 'attachment; filename=transactions_report.xlsx'
    return response

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_forms.html'
    success_url = reverse_lazy('login') # go to login page and message appears there

    def form_valid(self, form):
        messages.success(self.request, "Reset link sent! Check your email.")
        return super().form_valid(form)

class CustomPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'register/password_reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Password reset successfully done!")
        return super().form_valid(form)
    
    




    
    

    



            
    
  

    




            

    

