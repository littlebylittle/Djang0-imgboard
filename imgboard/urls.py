from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^$', include(admin.site.urls)),
                       )

urlpatterns += patterns('',
                        url(r'^', include('boards.urls')),
                        )


# Examples:
# url(r'^$', 'imgboard.views.home', name='home'),
# url(r'^imgboard/', include('imgboard.foo.urls')),
