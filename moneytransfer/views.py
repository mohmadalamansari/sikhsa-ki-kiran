from django.shortcuts import render
import datetime
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'moneytransfer/index.html')

@login_required()
def checkout(request):
	return render(request, 'moneytransfer/checkout.html')

@login_required()
def bank_page(request):
	now= datetime.datetime.now()
	return render(request, 'moneytransfer/bank-page.html', {'now':now})

@login_required()
def paytm_bank_page(request):
	now= datetime.datetime.now()
	return render(request, 'moneytransfer/paytm-bank-page.html', {'now':now})	

@login_required()
def success(request):
	return render(request, 'moneytransfer/success.html', )