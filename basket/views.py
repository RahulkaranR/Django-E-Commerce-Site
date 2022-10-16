from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from store.models import product 
from .basket import Basket

# Create your views here.

def basket_summery(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket':basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        Product = get_object_or_404(product, id=product_id)
        basket.add(Product=Product, qty=product_qty)
        qty = basket.__len__()
        response = JsonResponse({'qty':qty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        print(request.POST.get('productid'))
        basket.delete(Product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        
    return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        productid = int(request.POST.get('productid'))
        productqty = int(request.POST.get('productqty'))
        basket.update(productid=productid, productqty=productqty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        return response


