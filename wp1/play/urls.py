from django.urls import path

from . import views

urlpatterns = [
    path('play', views.index2, name='index'),
    path('adduser', views.adduser, name='adduser'),
    path('verify', views.verify, name='verify'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('listgames', views.listgames, name='listgames'),
    path('getgame', views.getgame, name='getgame'),
    path('getscore', views.getscore, name='getscore'),
	    path('speak', views.speak, name='speak'),
    path('listen', views.listen, name='listen'),

]
