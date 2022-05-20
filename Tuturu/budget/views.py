from django.http import HttpResponse
from django.shortcuts import render
from budget.models import Article
# Create your views here.
def index(request):
    article_obj = Article.objects.get(id=1)
    article_title = article_obj.title
    article_content = article_obj.content
    STRING = f"""<h1>{article_title}</h1>"""
    return render(request, "budget/index.html")

def sd(request, numero_sd):
    if numero_sd in [1, 2, 3]:
        return render(request, f"budget/sd{numero_sd}.html", context={})
    return render(request, "budget/sd_not_found.html")
