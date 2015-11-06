"""CZ3003 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DontCrysis import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^homepage/$', views.homepage),
    url(r'^homepage/map2$', views.homepage_map2),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^invalid/$', views.invalid_login),
    url(r'^login/$',  views.login),
    url(r'^loggedin/$', views.loggedin),
    url(r'^auth/$',  views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register_user),
    url(r'^register_success/$', views.register_success),
    url(r'^subscribe/$', views.createSubscriber),
    url(r'^subscriber_successful/$', views.subscriber_successful),
    url(r'^crisis/create/$', views.crisis_create, name='create-crisis'),
    url(r'^crisis/status/$', views.status_crisis, name='crises-created'),
    url(r'^user/addreportreceiver', views.addReportReceiver, name="add-report-receiver"),
    url(r'^user/reportreceiveradded', views.report_reciever_added, name="report-receiver-added"),
    url(r'^edit/(?P<pk>\d+)$', views.crisis_update, name='crisis_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.crisis_delete, name='crisis_delete'),
    url(r'^toggle/(?P<pk>\d+)$', views.crisis_toggle_active, name='crisis_toggle_active'),
]
