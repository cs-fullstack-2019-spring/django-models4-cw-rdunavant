from django.http import HttpResponse
from django.shortcuts import render
from .models import Mom, Child

# Create your views here.
def getmoms(request):
    moms=Mom.objects.all()
    for rpt in moms:
        print