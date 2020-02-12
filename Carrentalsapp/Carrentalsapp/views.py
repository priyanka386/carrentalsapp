

from django.shortcuts import render , get_object_or_404 , redirect 
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.decorators import login_required
from mycart.models import Vehicle , AddCart , Orders , User 
from django.urls import reverse

@login_required
def home(request):
    return render(request ,'home.html')


def my_order_list(request):

	id = request.GET.get("id")
	vehicle_obj = Vehicle.objects.get(id=id)
	add_cart = Orders.objects.create(vehicle = vehicle_obj ,payment_status= True) 
	cart_obj = Orders.objects.all()
	return render (request, 'mycart/list.html',{'my_order_list': cart_obj})


def order_details(request):
    info=Vehicle.objects.all()
    return render(request,'mycart/order.html',{'order_details':info})

def add_to_cart(request):
	# cart_obj = AddCart.objects.all()
	# if cart_obj:
	# 	cart_obj.delete()
	if request.method == 'POST':
		id = request.POST.get("id")
		product_obj = Vehicle.objects.get(id=id)
		total = product_obj.price
		product = AddCart.objects.create(user=request.user,vehicle=product_obj,grand_total=total)
		return redirect('show_cart_items')
		

def show_cart_items(request):
	cart_obj = Orders.objects.all()
	if cart_obj:		
		cart_obj.delete()
	show_cart_items = AddCart.objects.all()
	total=0
	for product in show_cart_items:
		total+=product.grand_total
	return render( request,'mycart/showcart.html',{'show_cart_items': show_cart_items,'total':total } )


def remove_from_cart(request):
	id = request.GET["id"]
	cart_item = AddCart.objects.get(id = id)
	cart_item.delete()
	return redirect('show_cart_items')









	



