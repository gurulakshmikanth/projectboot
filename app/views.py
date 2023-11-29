from django.shortcuts import render

# Create your views here.
def guru(request):
    return render(request,'guru.html')

def carousel(request):
    return render(request,'carousel.html')
def navbar(request):
    return render(request,'navbar.html')

def collapse(request):
    return render(request,'collapse.html')
def spinners(request):
    return render(request,'spinners.html')
def jumbotron(request):
    return render(request,'jumbotron.html')
def buttongroup(request):
    return render(request,'buttongroup.html')
def forms(request):
    return render(request,'forms.html')