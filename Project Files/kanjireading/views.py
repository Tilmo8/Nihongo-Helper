from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404	# Remove later if HttpResponse is not needed
from django.template import loader

from .models import Kanji

import random as Random

# Create your views here.
def index(request):
	return HttpResponse("Test success. Rendered \"kanji-reading.index\".")

def detail(request, kanji):
	if not isinstance(kanji, Kanji):
		kanji = get_object_or_404(Kanji, character=kanji)

	context = {
		'kanji': kanji,
		'complete_details': True,
	}

	return render(request, 'kanjireading/detail.html', context)

def random_kanji(request):
	kanji_list = get_list_or_404(Kanji)

	kanji = Random.choice(kanji_list)

	context = {
		'kanji': kanji,
		'complete_details': False,
	}

	return render(request, 'kanjireading/detail.html', context)


