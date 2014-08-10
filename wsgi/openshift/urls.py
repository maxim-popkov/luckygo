from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'', include('luckygo.urls', namespace='luckygo')),
    # url(r'^search/$', include('luckygo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# urlpatterns = patterns('luckygo.views',
# 	url(r'^$', 'index', name='index'),
# )
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()