from django.conf.urls import url

import views

urlpatterns = [
    url(r'^cached$', views.CachedEndpoint.as_view(), name='cached'),
    url(r'^not_cached$', views.NonCachedEndpoint.as_view(), name='not_cached')
]
