
from django.urls import path
# from expenses.views import home
# from . import views
# from expenses.views import HomeView
from expenses.views import RegisterView, DashBoard, Transactions, TransactionView, GoalCreateView, export_transactions, CustomPasswordResetView, CustomPasswordResetConfirm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
   # path('', views.home, name = "home"),
   # path('ghar/', HomeView.as_view(), name = "ghar")
   path('register/', RegisterView.as_view(), name = 'register'),
   path('', DashBoard.as_view(), name = 'home'),
   path('transaction/add/', Transactions.as_view(), name='transactions_add'),
   path("transaction/list/", TransactionView.as_view(), name="transaction_list"),
   path("goals/", GoalCreateView.as_view(), name='goals'),
   path('generate_report/', export_transactions, name='exports'),

    # ✅ LOGIN PAGE
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    # ✅ LOGOUT PAGE
    path(
        'account/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),


   # Enter Email 
   path('password_reset/', CustomPasswordResetView.as_view(template_name='registration/password_reset_forms.html'), name='password_reset'), #it have default tamplate_name = 'create you own path otherwise django will provide a default like registration/password_reset'
   # and also it have succsess_url = 'where to go next page like '/home/ and it inside a .as_view(here)'
   # step-2: email sent page
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

   # step-3 Reset Link Page
   path('reset/<uidb64>/<token>/', CustomPasswordResetConfirm.as_view(template_name='registration/password_reset_confirms.html'), name='password_reset_confirm'),
  
  #password reset complete


]

