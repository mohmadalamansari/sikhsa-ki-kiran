from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='money-transfer'),
	path('checkout/', views.checkout, name = 'checkout'),
	path('bank-page/', views.bank_page, name='bank-page'),
	path('paytm-bank-page/', views.paytm_bank_page, name ='paytm-bank-page'),
	path('paytm-bank-page/success/', views.success, name='success')
]