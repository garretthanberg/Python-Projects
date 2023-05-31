from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function will render the Home Page when requested.
def home(request):
    # This will retrieve the Transaction form.
    form = TransactionForm(data=request.POST or None)
    # This checks if the request methos is POST.
    if request.method == 'POST':
        # If the form is submitted, this will retrieve which account the user want to view.
        pk = request.POST['account']
        # This is a call balance function to render that account's Balance Sheet.
        return balance(request, pk)
    # This saves/passes the content to the template as a dictionary.
    content = {'form': form}
    # This adds the content of the form to the page.
    return render(request, 'checkbook/index.html', content)


# This function will render the Create New Account Page when requested.
def create_account(request):
    # This will retrieve the Account form.
    form = AccountForm(data=request.POST or None)
    # This checks if the request method is POST.
    if request.method == 'POST':
        # This checks to see if the submitted form is valid and if so, the form will be saved.
        if form.is_valid():
            form.save()  # This saves the new account.
            # This will redirect the user back to the home page.
            return redirect('index')
    # This saves/passes the content to the template as a dictionary.
    content = {'form': form}
    # This adds the content of the form to the page.
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function will render the Balance Page when requested.
def balance(request, pk):
    # This will retrieve the requested amount using its primary key.
    account = get_object_or_404(Account, pk=pk)
    # This will retrieve all of the account's transactions.
    transactions = Transaction.Transactions.filter(account=pk)
    # This will create account total variable, starting with initial deposit value.
    current_total = account.initial_deposit
    # This will create a dictionary into which transaction information will be placed.
    table_contents = {}
    # This will loop through transactions and determine which is a deposit or a withdrawal.
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount  # If deposit adds amount to the balance:
            # It will add transaction and total to the dictionary.
            table_contents.update({t: current_total})
        else:
            # If withdraw subtracts amount from the balance:
            current_total -= t.amount
            # It will add transaction and total to the dictionary.
            table_contents.update({t: current_total})
    # This will pass account, account total balance, and transaction information to the template.
    content = {'account': account,
               'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the Transaction Page when requested.
def transaction(request):
    # This will retrieve the Transaction form.
    form = TransactionForm(data=request.POST or None)
    # This checks if the request method is POST.
    if request.method == 'POST':
        # This checks to see if the submitted form is valid and if so, the form will be saved.
        if form.is_valid():
            # This will retrieve which account the transaction was for.
            pk = request.POST['account']
            form.save()  # This saves the transaction form.
            # This will render the balance of the accounts Balance Sheet.
            return balance(request, pk)
    # This saves/passes the content to the template as a dictionary.
    content = {'form': form}
    # This adds the content of the form to the page.
    return render(request, 'checkbook/AddTransaction.html', content)
