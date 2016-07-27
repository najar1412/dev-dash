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
)



"""



url(r'^home/$', home),
url(r'^stat/$', stat),
url(r'^send_note/$', send_note),
url(r'^post_note/$', post_note),
url(r'^new_project/$', new_project),
url(r'^del_project/$', del_project),
url(r'^media/$', media),
url(r'^project/$', project),
url(r'^del_note/$', del_note),
url(r'^setting/$', setting),

url(r'^thank/$', setting),
url(r'^note/$', note),
url(r'^almanac/$', almanac),
url(r'^upload_media/$', upload_media),
"""