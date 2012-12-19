from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indras_net.views.home', name='home'),
    # url(r'^indras_net/', include('indras_net.foo.urls')),
    url(r'^leaves/$', 'leaves.views.index'),
    url(r'^leaves/authors/$', 'leaves.views.authors'),
    url(r'^leaves/sources/$', 'leaves.views.sources'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
