from django.forms import ModelForm
from .models import Account, Transaction


# This creates an Account Form based on Account Model.
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# This creates a Transaction Form based on Transaction Model.
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
