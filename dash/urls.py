"""dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin
from dashcore.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^dash/$', dash),
    url(r'^setting/$', setting),
    url(r'^update_member/$', update_member),
    url(r'^project/$', project),
    url(r'^project_new/$', project_new),
    url(r'^project_del/$', project_del),
    url(r'^project_asset/$', project_asset),
    url(r'^rank/$', rank),
    url(r'^asset/$', asset),
    url(r'^asset_new/$', asset_new),
    url(r'^asset_dash/$', asset_dash),

)
