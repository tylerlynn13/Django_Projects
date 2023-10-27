from django.urls import path
from . import views


urlpatterns = [
    # sets url path to home page index.html.
    path('', views.home, name='index'),
    # sets the url path to create new account page CreateNewAccount.html.
    path('create/', views.create_account, name='create'),
    # sets the url path tp balance sheet page BalanceSheet.html.
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets url path to add new transaction page AddNewTransaction.html.
    path('transaction/', views.transaction, name='transaction')
]