from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from budget.models import Article

# Create your views here.
def index(request):
    article_obj = Article.objects.get(id=1)
    queryset = Article.objects.all()
    context={
        "queryset": queryset,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    STRING = render_to_string("budget/index.html",context=context)
    return HttpResponse(STRING)

def sd(request, numero_sd):
    context={}
    if numero_sd in [1, 2, 3]:
        return render(request, f"articles/sd{numero_sd}.html", context=context)
    return render(request, "articles/sd_not_found.html")
