from django.shortcuts import render
def index(request):
    return render(request, "index.html")
def loan(request):
    return render(request, "loan.html")
def credit_card(request):
    return render(request, "credit_card.html")
def banking(request):
    return render(request, "banking.html")
def insurance(request):
    return render(request, "insurance.html")
def mutual_fund(request):
    return render(request, "mutual_fund.html")
def business_account(request):
    return render(request, "business_account.html")

# Create your views here.
