from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import redesSociales.views
import baskets.views
import products.views
import providers.views
import session.views
import home.views
import shoppingItems.views
import payment.views
import deliveries.views



# Examples:
# url(r'^$', 'main.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', redesSociales.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^baskets/', baskets.views.get_baskets, name='baskets'),
    url(r'^products/', products.views.get_products, name='products'),
    url(r'^addProduct/(\d+)/(.+)', shoppingItems.views.addProduct, name='addProduct'),
    url(r'^deleteProduct/(\d+)', shoppingItems.views.deleteProduct, name='deleteProduct'),
    url(r'^shoppingItems', shoppingItems.views.get_shoppingItems, name='shoppingItems'),
    url(r'^certifiedProducts/', products.views.get_certified_products, name='certifiedProducts'),
    url(r'^providers/', providers.views.get_providers, name='providers'),
    url(r'^details/(\d+)', products.views.details, name='details'),
    url(r'^login', session.views.login_request, name='login'),
    url(r'^islogged/', session.views.is_logged_user, name='isLoggedUser'),
    url(r'^logout/', session.views.logout_user, name='logout'),
    url(r'^certifiedProviders/', providers.views.get_providers_certified, name='certifiedProviders'),
    url(r'^payment', payment.views.pay_cart, name='payCart'),
    url(r'^home', home.views.home, name='home'),
    url(r'^deliveries', deliveries.views.get_dates, name='deliveries'),
]
