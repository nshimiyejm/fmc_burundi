"""fmc_bdi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# Add these two line to pull modules used for files 
from django.conf import settings
from django.conf.urls.static import static

import leadership.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaders', leadership.views.profiles, name='profiles'), 
    path('', leadership.views.index, name='home'), 
    path('leadership/<int:leader_id>', leadership.views.bio, name='bio'),
    path('about', leadership.views.history, name='about'),
]

# These two will be used to display static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
