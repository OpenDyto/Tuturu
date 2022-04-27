from django.urls import path
from .views import index, sd
urlpatterns = [
    path('', index, name="budget-index"),
    path('sd<int:numero_sd>/', sd, name="budget-sd"),
]
