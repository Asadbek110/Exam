from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from blog.models import Product, Customer

# Create your views here.


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'blog/product-detail.html', context)


def customer_list(request):
    customers = Customer.objects.all()
    search_query = request.GET.get('search')
    paginator = Paginator(customers, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if search_query:
        page_obj = customers.filter(Q(name__icontains=search_query)|Q(email__icontains=search_query))
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/customers.html',context)


def customer_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    context = {
        'customer' :customer,
    }

    return render(request, 'blog/customer-details.html',context)


def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer_details = CustomerDetails.objects.get(customer=customer)
    if request.method == 'POST':
        form = CustomerDetails(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_details', customer_id=customer.id)
        else:
            form = CustomerDetails(instance=customer)
        return render(request, 'blog/customer-details.html', {'customer': customer, 'form': form})


def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customer_details', customer_id=customer.id)


