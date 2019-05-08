from django.shortcuts import render
from django.http import HttpResponse	# Remove later if HttpResponse is not needed

# Create your views here.
def index(request):
	return HttpResponse("Test success. Rendered \"kanji-reading.index\".")