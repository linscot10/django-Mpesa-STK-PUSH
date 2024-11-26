from django.shortcuts import render
from django.http import HttpResponse

import requests

from .credentials import MpesaAccessToken,MpesaPassword
# ,get_mpesa_access_token

# Create your views here.

def home(request):
    return render(request,'home.html')

def pay(request):
    return render(request,'pay.html')



def stk(request):
    # access_token = get_mpesa_access_token()
    if request.method=="POST":
        phone =request.POST['phone']
        amount =request.POST['amount']
        access_token=MpesaAccessToken.mpesa_access_token
        api_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers={"Authorization":"Bearer %s" % access_token}
        request={
            "BusinessShortCode": MpesaPassword.bussiness_short_code,    
            "Password": MpesaPassword.decode_password,    
            "Timestamp":MpesaPassword.lipa_time,    
            "TransactionType": "CustomerPayBillOnline",    
            "Amount": amount,    
            "PartyA":phone,    
            "PartyB": MpesaPassword.bussiness_short_code,    
            "PhoneNumber":phone,    
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",    
            "AccountReference":"Lawrence Scott",    
            "TransactionDesc":"Test"
        }
        
        response =requests.post(api_url,json=request,headers=headers)
        return HttpResponse("Success: " + response.text)
    else:
        return HttpResponse("Invalid request method")

