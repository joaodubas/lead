from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lead.views.home', name='home'),
    url(r'^contact/$', 'apps.contact.views.contact', name='contact'),
    url(r'^signin/$', 'apps.users.views.signin', name='signin'),
    url(r'^signout/$', 'apps.users.views.signout', name='signout'),

    url(r'^admin/', include(admin.site.urls)),
)
