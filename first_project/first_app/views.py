from django.shortcuts import render
from django.http import HttpResponse
# Imported HTTPREsponse Object from Django HTTP MOdule

# Create your views here.
# Each view for this app is going to exist within that views.py file as its own function.

# We just created one view called Index, and each view is also going to take in at least one argument
# The HttpObject is called request from django.http
# Each view must return a httpresponse object

def index(request):
    return HttpResponse("<h1>Hello World</h1>")
# You can pass html content in output