from django.conf.urls import include, url
from django.contrib import admin
from .views import home, home_files
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', home, name='home'),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),

]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
