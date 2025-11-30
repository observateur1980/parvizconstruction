from  . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('video', views.Video.as_view(), name='video'),
    path('gallery', views.Gallery.as_view(), name='gallery'),
    path('project', views.Project.as_view(), name='project'),



    path('designbuild', views.Designbuild.as_view(), name='designbuild'),
    path('newconstruction', views.Newconstruction.as_view(), name='newconstruction'),
    path('kitchen', views.Kitchen.as_view(), name='kitchen'),
    path('bathroom', views.Bathroom.as_view(), name='bathroom'),
    path('garage', views.Garage.as_view(), name='garage'),
    path('homeremodel', views.Homeremodel.as_view(), name='homeremodel'),
    path('homeadditions', views.Homeadditions.as_view(), name='homeadditions'),
    path('planspermits', views.Planspermits.as_view(), name='planspermits'),


    path('fatjo', views.Fatjo.as_view(), name='fatjo'),
    path('sjdowntown', views.Sjdowntown.as_view(), name='sjdowntown'),
    path('laterrace', views.Laterrace.as_view(), name='laterrace'),
    path('cheltenham', views.Cheltenham.as_view(), name='cheltenham'),
    path('piper', views.Piper.as_view(), name='piper'),
    path('daves', views.Daves.as_view(), name='daves'),




    path('create_lead/', views.create_lead, name='create_lead'),
    path('create_lead/success/', views.create_lead_success, name='create_lead_success'),

    path("geoip-test/", views.geoip_test, name="geoip_test"),


   
]
