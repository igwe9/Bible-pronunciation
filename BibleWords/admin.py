from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
	list_display = ('word', 'audio_src','date_created')
	search_fields = ['word']
	readonly_fields = ('word','audio_src','date_created')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Word, WordAdmin)


