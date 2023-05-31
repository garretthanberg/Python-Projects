from django.urls import path
from . import views


urlpatterns = [
    # This sets the url path to hom page index.html.
    path('', views.home, name='index'),
    # This sets the url path to Create New Account page CreateNewAccount.html.
    path('create/', views.create_account, name='create'),
    # This sets the url path to Balance sheet page Balancesheet.html.
    # This also allows the Balance Sheet to be displayed using a primary key.
    path('<int:pk>/balance/', views.balance, name='balance'),
    # This sets the url path to Add New Transaction page AddNewTransaction.html.
    path('transaction/', views.transaction, name='transaction'),
    # This allows the Balance Sheet to be displayed using a primary key.
]
