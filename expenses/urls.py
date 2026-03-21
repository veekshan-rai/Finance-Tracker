
from django.urls import path
# from expenses.views import home
# from . import views
# from expenses.views import HomeView
from expenses.views import RegisterView, DashBoard, Transactions, TransactionView, GoalCreateView, export_transactions

urlpatterns = [
   # path('', views.home, name = "home"),
   # path('ghar/', HomeView.as_view(), name = "ghar")
   path('register/', RegisterView.as_view(), name = 'register'),
   path('', DashBoard.as_view(), name = 'home'),
   path('transaction/add/', Transactions.as_view(), name='transactions_add'),
   path("transaction/list/", TransactionView.as_view(), name="transaction_list"),
   path("goals/", GoalCreateView.as_view(), name='goals'),
   path('generate_report/', export_transactions, name='exports'),
]

