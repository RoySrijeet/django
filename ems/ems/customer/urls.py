from django.urls import path
from . import views

urlpatterns = [
    path('register.html', views.register_view, name='register'),
    path('login.html', views.login_view, name='login'),
    path('logout.html', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('login.html', views.login_new, name='login'),
    path('wedding.html', views.wedding, name='wedding'),
    path('birthday.html', views.birthday, name='birthday'),
    path('anniversary.html', views.anniversary, name='anniversary'),
    path('corporate.html', views.corporate, name='corporate'),
    path('cultural.html', views.cultural, name='cultural'),
    path('customize.html', views.customize, name='customize'),
    path('submit_details.html', views.submit_details, name='submit_details')
]
