"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mysite import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.home),
    path('power/',views.pract),
    path('about-us/',views.about,name="about"),
    path('service/',views.service),
    path('contact-us/',views.contact),
    path('form/',views.form),
    path('postform/',views.postform),
    # path('project/', views.projects),
    # # path('project/<projectid>', views.projectdetail),
    # path('project/<int:projectid>',views.projectdetail),
    # path('project/<str:projectid>',views.projectdetail2),
    # path('project/<slug:projectid>',views.projectdetail3),        
    # path('about/', views.aboutUS),
    # path('contact/',views.contactus),
    # path('power/',views.powerranger),
]
