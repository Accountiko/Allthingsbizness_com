"""
URL configuration for atb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog',AllBlogsView.as_view(),name = 'allblogs'),
    path('blog/<slug:slug>',BlogDetailView.as_view(),name = 'details'),

    path('',homeview,name = 'home'),
    path('about-founder/',aboutfounderview,name = 'about-founder'),
    path('aboutus/',aboutusview,name = 'aboutus'),
    path('service/',serviceview,name = 'service'),
    path('contactus/',contactusview,name = 'contactus'),

    path('getemail/',getmails,name = 'getemail'),
    path('getcontactus/',getcontactus,name = 'getcontactus'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
