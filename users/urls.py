from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("Users app OK ✅")

urlpatterns = [
    path('', test),
]   