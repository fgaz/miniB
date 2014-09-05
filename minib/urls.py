from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minib.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^>>(?P<postNumber>\d+)', 'board.views.board'),
    url(r'^(?P<pageNumber>\d+)', 'board.views.board'),
    url(r'^', 'board.views.board', {'pageNumber': 1}),
)
