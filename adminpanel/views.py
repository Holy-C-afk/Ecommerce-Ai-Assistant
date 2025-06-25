from django.shortcuts import render
from .models import Analytics

# Create your views here.

def dashboard(request):
    analytics = Analytics.objects.first()
    return render(request, 'adminpanel/dashboard.html', {'analytics': analytics})
