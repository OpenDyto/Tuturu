from django import forms
from django.forms import ModelForm
from budget.models import Article



class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = ['title', 'content']



class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

def clean(self):
    data = self.cleaned_data
    title = data.get('title')
    qs = Article.objects.all().filter(title_icontains=title)
    return data
