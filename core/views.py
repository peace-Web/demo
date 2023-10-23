from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid
# Create your views here.
def home(request):

    host = request.get_host()
    
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '0.01',
        'item_name': 'product test',
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('success')}",
        'cancel_url': f"http://{host}{reverse('fail')}",
    }
    paypal_payment = PayPalPaymentsForm(initial = paypal_checkout)

    context = {
        'paypal': paypal_payment
    }

    return render(request, "core/home.html", context)
    

def success(request):
    return render(request, 'core/success.html')

def fail(request):
    return render(request, 'core/fail.html')