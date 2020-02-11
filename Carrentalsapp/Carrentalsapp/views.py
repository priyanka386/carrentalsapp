

from django.shortcuts import render , get_object_or_404 , redirect 
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.decorators import login_required
from mycart.models import Vehicle , AddCart , Orders , User 
from django.urls import reverse

@login_required
def home(request):
    return render(request ,'home.html')


def myorder_list(request):
	order_item = AddCart.objects.all()
	payment_status = items.payment_status
	return render( request, 'mycart/list.html',{'myorder_list': order_item})


def order_details(request):
    info=Vehicle.objects.all()
    return render(request,'mycart/order.html',{'order_details':info})


def add_to_cart(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		product_obj = Vehicle.objects.get(id=id)
		total = product_obj.price
		product = AddCart.objects.create(user=request.user,vehicle=product_obj,grand_total=total)
		return redirect('show_cart_items')
		

def show_cart_items(request):
	show_cart_items = AddCart.objects.all()
	total=0
	for product in show_cart_items:
		total+=product.grand_total
	return render( request,'mycart/showcart.html',{'show_cart_items': show_cart_items,'total':total } )


	







	



