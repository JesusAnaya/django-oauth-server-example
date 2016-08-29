from django.views.generic import TemplateView, RedirectView
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^accounts/login/$', TemplateView.as_view(template_name='account/login.html'), name='login'),
    url(r'^accounts/logout/$', TemplateView.as_view(template_name='account/logout.html'), name='logout'),
    url(r'^accounts/forgot-passwrod/$', TemplateView.as_view(template_name='account/forgot_password.html'), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
