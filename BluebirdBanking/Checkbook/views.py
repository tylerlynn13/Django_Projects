from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction
# Create your views here.


# this function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieve transaction form
    # checks if request method is post
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieve which account the user wants
        return balance(request, pk)  # call balacance function to render that accounts balance sheet
    content = {'form': form}  # pass content to the templlate in a directory
    # adds content of form to page
    return render(request, 'checkbook/index.html', content)


# this function will render the create new account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve account form
    # checks if request method is post
    if request.method == 'POST':
        if form.is_valid():  # check to see if the submitted form is valid if so save
            form.save()  # saves new account
            return redirect('index')  # returns user back to home page
    content = {'form': form}  # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieve account using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieve all of that accounts transactions
    current_total = account.initial_deposit  # create account total variable, starting with initial deposit
    table_contents = {}  # creates a dictionary into which transaction info will be placed
    for t in transactions:  # loop through transaction and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit add amount to balance
            table_contents.update({t: current_total})  # add transactuon and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtract amount from balance
            table_contents.update({t: current_total})  # add transaction and total to dictionary
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieve the transaction form
    # checks if request method is post
    if request.method == 'POST':
        if form.is_valid():  # check to see if submitted form is valid if so save
            pk = request.POST['account']  # retrieve which account the transaction was for
            form.save()  # saves the transaction form
            return balance(request, pk)  # renders balance of the accounts balance sheet
    # pass content to the template in a dictionary
    content = {'form': form}
    # adds content of form  to page
    return render(request, 'checkbook/AddTransaction.html', content)

