#from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, "budget/index.html")

def sd(request, numero_sd):
    if numero_sd in [1, 2, 3]:
        return render(request, f"budget/sd{numero_sd}.html", context={})
    return render(request, "budget/sd_not_found.html")
