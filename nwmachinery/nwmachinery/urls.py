from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home_page', name='home'),
    url(r'^Software', 'website.views.software', name='software'),
    url(r'^softwaredownload', 'website.views.software_download', name='softwaredownload'),
    url(r'^Inspections', 'website.views.inspections', name='inspections'),
    url(r'^About', 'website.views.about', name='about'),
    url(r'^Contact', 'website.views.contact', name='contact'),
    url(r'^softwarepurchase', 'website.views.software_purchase', name='softwarepurchase'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
