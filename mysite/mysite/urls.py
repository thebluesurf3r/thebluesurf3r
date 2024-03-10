"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from main.views import home_view, aboutme_view, techskills_view, profskills_view, projects_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('aboutme/', aboutme_view, name='aboutme'),
    path('technical_skills/', techskills_view, name='technical_skills'),
    path('professional_skills/', profskills_view, name='professional_skills'),
    path('projects/', projects_view, name='projects'),
    path('contact/', contact_view, name='contact'),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)