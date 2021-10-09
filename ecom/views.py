from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
import logging
from django.views.decorators.csrf import csrf_exempt
from Paytm import checksum

logger = logging.getLogger(__name__)
# Create your views here.
MERCHANT_KEY = 'bKMfNxPPf_QdZppa'

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'ecom/index.html', params)


def about(request):
    return render(request, 'ecom/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        desc = request.POST.get('desc',"")
        contact_var = Contact(contact_name=name, contact_email=email, contact_phone=phone, contact_desc=desc)
        contact_var.save()
        query = True
        return render(request, 'ecom/contact.html', {'query': query})
    return render(request, 'ecom/contact.html')


def tracker(request):
    if request.method=="POST":
        order_id = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                print(order[0].items_json)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'ecom/tracker.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'ecom/prodview.html', {'product':product[0]})


def search(request):
    return render(request, 'ecom/search.html')


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        amount= request.POST.get('amount', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order_var = Order(items_json=items_json, amount=amount, name=name, email=email, address=address, city=city, state=state, zip=zip_code, phone_number=phone)
        order_var.save()
        update = OrderUpdate(order_id=order_var.order_id, update_desc="The order has been placed.")
        update.save()
        thank=True
        id = order_var.order_id
        request.session['order'] = order_var.order_id
        request.session['amount_var'] = order_var.amount
        request.session['email_var'] = order_var.email
        #return render(request, 'ecom/checkout.html', {'thank':thank, 'id':id})
        # request paytm to transfer amount to your account after succesfull payment


    return render(request, 'ecom/checkout.html')


def placeorder(request):
    if request.method=="POST":
        order = request.session['order']
        amount = request.session['amount_var']
        email = request.session['email_var']
        param_dict = {
            'MID': 'DIY12386817555501617',
            'ORDER_ID': str(order),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': str(email),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/ecom/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'ecom/paytm.html', {'param_dict':param_dict})
    return render(request, 'ecom/checkout.html')


@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
    return HttpResponse('done')
    pass
