from django.shortcuts import render
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    context = {
        "deals": records
    }
    return render(request, "index.html", context)