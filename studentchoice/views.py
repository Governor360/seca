from django.shortcuts import render
from django.http import HttpResponse
from studentchoice.models import Appinfo, Category
from . models import *


# Create your views here.

def index(request):
    info = Appinfo.objects.get(pk=1)
    
    context ={
        'info' :info,
    }
    
    
    return render(request, 'index.html', context)

def awardee(request):
    info = Appinfo.objects.get(pk=1)
    nominee = Category.objects.all()
    
    context ={
        'info' :info,
        'nominee' :nominee,
    }
    return render(request, 'awardee.html', context)

def actyuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'actyuli.html', context)

def actorigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'actorigba.html', context)

def actressuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'actressuli.html', context)

def actressigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'actressigba.html', context)
def mostinigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mostinigba.html', context)
def mostinuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mostinuli.html', context)
def mostbigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mostbigba.html', context)
def mostbuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mostbuli.html', context)
def stdiigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stdiigba.html', context)
def stdiuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stdiuli.html', context)
def maigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'maigba.html', context)
def mauli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mauli.html', context)
def fmaigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmaigba.html', context)
def fmauli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmauli.html', context)
def stddjigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stddjigba.html', context)
def actyuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'actyuli.html', context)
def stddjuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stddjuli.html', context)
def fctigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fctigba.html', context)
def fctuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fctuli.html', context)
def matuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'matuli.html', context)
def matigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'matigba.html', context)
def fmtigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmtigba.html', context)
def contentigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'contentigba.html', context)
def contentuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'contentuli.html', context)
def fmtuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmtuli.html', context)

def comigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'comigba.html', context)

def comuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'comuli.html', context)

def skitigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'skitigba.html', context)

def skituli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'skituli.html', context)

def hypemanigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'hypemanigba.html', context)

def hypemanuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'hypemanuli.html', context)

def schigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'schigba.html', context)

def schuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'schuli.html', context)

def spigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'spigba.html', context)

def spuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'spuli.html', context)

def mmuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mmuli.html', context)

def mmigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mmigba.html', context)

def fmigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmigba.html', context)

def fmuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmuli.html', context)

def stpuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stpuli.html', context)

def stpigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stpigba.html', context)

def stvigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stvigba.html', context)

def stvuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stvuli.html', context)

def stppigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stppigba.html', context)
def stppuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'stppuli.html', context)

def courseigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'courseigba.html', context)

def courseuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'courseuli.html', context)

def mdigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mdigba.html', context)

def fmdigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmdigba.html', context)

def mduli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'mduli.html', context)

def fmduli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'fmduli.html', context)

def otyigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'otyuli.html', context)

def eveigba(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'eveigba.html', context)

def eveuli(request):
    info = Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'eveuli.html', context)
def pay(request):
    info =Appinfo.objects.get(pk=1)
    
    context={
        'info' :info,
    }
    return render(request, 'pay.html', context)

