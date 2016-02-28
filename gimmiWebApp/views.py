from django.shortcuts import render
# -^ This import came default with the file. I have no use for it thus far, but I wonder why it was placed here..

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, World!. Welcome to the Gimmi Web App!")
