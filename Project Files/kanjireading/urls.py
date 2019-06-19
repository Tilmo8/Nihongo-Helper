from django.urls import path

from . import views

app_name = 'kanji'
urlpatterns = [
    path('', views.index, name='index'),
    path('random', views.random_kanji, name='random'),
    path('detail/<str:kanji>', views.detail, name='detail')
]