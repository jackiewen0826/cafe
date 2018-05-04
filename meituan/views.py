from django.shortcuts import render
from . models import Order
def home_page(request):
	orders = Order.objects.all()
	if request.method == 'POST':
		our_dish = request.POST.get('dish')
		our_address = request.POST.get('address')
		order_obj = Order.objects.create(
			dish=our_dish,
			address=our_address
		)
		orders = Order.objects.all()
		return render(request, 'meituan/home_page.html', {'orders': orders,})
	return render(request, 'meituan/home_page.html', {'orders': orders,})
