from django.contrib import admin
from leaves.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'author')

admin.site.register(Quote)
