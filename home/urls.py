from  . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('project', views.Project.as_view(), name='project'),
    path('gallery', views.Gallery.as_view(), name='gallery'),
    path('video', views.Video.as_view(), name='video'),
    path('kitchen', views.Kitchen.as_view(), name='kitchen'),
    path("geoip-test/", views.geoip_test, name="geoip_test"),


    path('getquote', views.GetQuote.as_view(), name='getquote'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('contact_local', views.Contact_Local.as_view(), name='contact_local'),
    path('workflow', views.WorkFlow.as_view(), name='workflow'),
    path('louveredroof', views.LouveredRoof.as_view(), name='louveredroof'),
    path('sunroom', views.Sunroom.as_view(), name='sunroom'),
    path('retractable', views.Retractable.as_view(), name='retractable'),
    path('win-door', views.WinDoor.as_view(), name='win-door'),
    path('sunshade', views.Sunshade.as_view(), name='sunshade'),
    path('success_sent', views.SuccessSent.as_view(), name='success_sent'),

   
]
