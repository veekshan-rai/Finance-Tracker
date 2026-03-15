
from django.urls import path
# from expenses.views import home
# from . import views
# from expenses.views import HomeView
from expenses.views import RegisterView, DashBoard, Transactions

urlpatterns = [
   # path('', views.home, name = "home"),
   # path('ghar/', HomeView.as_view(), name = "ghar")
   path('register/', RegisterView.as_view(), name = 'register'),
   path('', DashBoard.as_view(), name = 'home'),
   path('transaction/add/', Transactions.as_view(), name='transactions_add')
]

