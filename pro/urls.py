"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path(
        'add-friend/',
        views.add_friend,
        name='add_friend'
    ),

    path(
        'add-expense/',
        views.add_expense,
        name='add_expense'
    ),

    path(
        'delete-expense/<int:id>/',
        views.delete_expense,
        name='delete_expense'
    ),

    path(
        'update-expense/<int:id>/',
        views.update_expense,
        name='update_expense'
    ),

]