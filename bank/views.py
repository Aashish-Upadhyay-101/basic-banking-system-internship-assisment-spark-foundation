from django.shortcuts import render, redirect
from .models import Customer


def home(request):
    return render(request, "bank/index.html")

def customers(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "bank/customers.html", context=context)

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    context = {"customer": customer}
    return render(request, "bank/customer_detail.html", context=context)

def transfer_balance(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    if request.method == "POST":
        data = request.body.decode("utf-8").split("&")
        customer = data[1].split('=')[1]
        amount = data[2].split('=')[1]
        customer = Customer.objects.get(user__username=customer)
        try:
            customer.balance += int(amount)
            customer.save()
        except:
            print("error")
        return redirect("bank:customers")
    return render(request, "bank/transfer.html", context=context)