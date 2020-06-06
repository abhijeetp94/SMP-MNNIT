from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SMP'

# Pipeline for the website.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('main_dark/', views.main_dark, name = "home_dark"),
    path('about_us/', views.about_us, name = "about_us"),
    path('general_info/', views.general_info, name = "general_info"),
    path('academics/', views.academics, name = "academics"),
    path('campus_life/', views.campus_life, name = "campus_life"),
    path('extra_curricular/', views.extra_curricular, name = "extra_curricular"),
    path('extra1/', views.extra1, name = "extra_curricular"),
    path('events/', views.events, name = "events"),
    path('clubs/', views.clubs, name = "clubs"),
    path('sports/', views.sports, name = "sports"),
    path('FAQ/', views.FAQ, name = "FAQ"),
    path('login/', views.loginbase, name = "loginbase"),
    path('contacts/', views.contacts, name = "contacts"),
    path('details/', views.details, name = "details"), 
    path('details/<str:usn>/', views.profile, name = "profile"), 
    path('resources/', views.resources, name = "resources"),
    path('Read_More/', views.readmore, name = "readmore"),
    path('logout/', views.logout_request, name = "logout_request"),

]