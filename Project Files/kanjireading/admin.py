from django.contrib import admin

from .models import Kanji, Reading, KanjiReading

class KanjiReadingInLine(admin.TabularInline):
	model = KanjiReading
	extra = 1

class KanjiAdmin(admin.ModelAdmin):
	inlines = (KanjiReadingInLine,)


# Register your models here.
admin.site.register(Kanji, KanjiAdmin)
admin.site.register(Reading)