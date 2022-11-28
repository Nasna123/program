from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun1(request):
    return HttpResponse("succesfully created")
def amstrong(request):
    return render(request,'amstrong.html')
def factorial(request):
    return render(request,'factorial.html')

def fibinocci(request):
    return render(request,'fibinocci.html')
def hcf(request):
    return render(request,'hcf.html')

def lcm(request):
    return render(request,'lcm.html')

def palindrome(request):
    return render(request,'palindrome.html')
def perfectno(request):
    return render(request,'perfectno.html')
def printfactors(request):
    return render(request,'printfactors.html')
def reversestring(request):
    return render(request,'reversestring.html')

def sortnumbers(request):
    return render(request,'sortnumbers.html')
def sumofdigits(request):
    return render(request,'sumofdigits.html')
def sumofprimeno(request):
    return render(request,'sumofprimeno.html')










