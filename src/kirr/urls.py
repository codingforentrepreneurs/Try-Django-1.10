"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from shortener.views import kirr_redirect_view, KirrCBView

# DO NOT DO
# from shortener import views
# from another_app.views import views

urlpatterns = [
    url(r'^new-admin/', admin.site.urls),
    url(r'^a/(?P<shortcode>[\w-]+)/$', kirr_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+)/$', KirrCBView.as_view()), #joincfe.com/projects/ python regex

    # DO NOT DO 
    #url(r'^abc/$', 'shortener.views.kirr_redirect_view' ),
    # url(r'^abc/$', views.kirr_redirect_view ),
]
