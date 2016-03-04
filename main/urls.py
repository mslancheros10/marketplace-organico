from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import redesSociales.views

# Examples:
# url(r'^$', 'main.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', redesSociales.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
