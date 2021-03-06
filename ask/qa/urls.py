"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from qa import views
from django.urls import re_path, path

urlpatterns = [
    path('', views.test),
    re_path(r'^login/', views.test),
    re_path(r'^signup/', views.test),
    re_path(r'^question/(\<(\d+)\>)/', views.test),
    re_path(r'^ask/', views.test),
    re_path(r'^popular/', views.test),
    re_path(r'^new/',views.test)
]
