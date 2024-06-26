"""
URL configuration for HTML_Form01 project.

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
from django.conf.urls import include
from mysite import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index),
    path('get_example/', views.get_example),
    path('<int:pid>/<str:del_pass>', views.index),
    path('list/', views.listing),
    path('post/', views.posting),
    path('contact/', views.contact),
    path('post2db/', views.post2db),
    path('captcha/', include('captcha.urls')),
]
