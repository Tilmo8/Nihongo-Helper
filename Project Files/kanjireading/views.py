from django.shortcuts import render
from django.http import HttpResponse, Http404	# Remove later if HttpResponse is not needed
from django.template import loader

from .models import Kanji

import random as Random

# Create your views here.
def index(request):
	return HttpResponse("Test success. Rendered \"kanji-reading.index\".")

def detail(request, kanji):
	if not isinstance(kanji, Kanji):
		kanji_lookup = Kanji.objects.filter(character__exact=kanji)

		if not kanji_lookup.exists():
			raise Http404("Kanji not found")
		else:
			kanji = kanji_lookup[0]

	template = loader.get_template('kanjireading/detail.html')
	context = {
		'kanji': kanji
	}

	return HttpResponse(template.render(context, request))
	# return HttpResponse(f"<h1>HAI, you're looking at kanji: {kanji.character} <h1>")

def random_kanji(request):
	kanji_list = list(Kanji.objects.all())

	list_length = len(kanji_list)

	if list_length <= 0:
		raise Http404("Kanji not found")

	kanji = Random.choice(kanji_list)

	template = loader.get_template('kanjireading/detail.html')
	context = {
		'kanji': kanji
	}

	return HttpResponse(template.render(context, request))


