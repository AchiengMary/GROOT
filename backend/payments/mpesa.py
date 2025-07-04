import requests
from requests.auth import HTTPBasicAuth

def send_stk_push(phone, amount):
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": "174379",
        "Password": generate_password(),
        "Timestamp": timestamp(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": "174379",
        "PhoneNumber": phone,
        "CallBackURL": "https://yourdomain.com/payment/callback",
        "AccountReference": "OvarianCyst",
        "TransactionDesc": "Cyst Treatment Payment"
    }
    return requests.post(url, json=payload, headers=headers)
