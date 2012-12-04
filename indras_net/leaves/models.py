from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.TextField(unique=True, blank=True)

    def __unicode__(self):
        return self.name


class Source(models.Model):
    SOURCE_CATEGORY_CHOICES = (
        ('Book', 'Book'),
        ('Website', 'Website'),
        ('Film', 'Film'),
    )
    name = models.CharField(max_length=400, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=400, choices=SOURCE_CATEGORY_CHOICES, default='Website')
    url = models.URLField(max_length=2048, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Quote(models.Model):
    body = models.TextField(unique=True)
    author = models.ForeignKey(Author)
    source = models.ForeignKey(Source)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.body

    def truncated_body(self):
        return self.body[:100] + '...'
