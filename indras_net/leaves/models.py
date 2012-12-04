from django.db import models


class Quote(models.Model):
    body = models.TextField(unique=True)
    author = models.CharField(max_length=400, default='Unknown')
    source = models.URLField(max_length=2048, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.body + '\n- ' + self.author

    def get_truncated_body(self):
        return self.body[:100] + '...'
