#DEVS1
# from django.http import HttpResponse
from datetime import datetime
#[context={"date": datetime.today()}]
# --> django template filter // filtre utilisable dans {}
from django.shortcuts import render
from budget.models import Article

#DEVS1
# def index2(request):
#    return HttpResponse("<h1>Tuturu</h1>")
def index(request):
    return render(request, "ns/index.html", context={"date": datetime.today()})

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title, content=content)
    context={}
    return render(request, "ns/create.html",context=context)
