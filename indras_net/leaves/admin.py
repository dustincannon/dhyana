from django.contrib import admin
from leaves.models import Quote, Author, Source

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('truncated_body', 'author', 'source')

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Author)
admin.site.register(Source)
