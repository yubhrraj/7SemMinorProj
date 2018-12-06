from django.conf.urls import url
from base_app import views

app_name = 'base_app'
urlpatterns = [
    url(r'^userlogin/$', views.userlogin, name="userlogin"),
    url(r'^register/$', views.register, name="register"),
    url(r'^main/$', views.mainpage, name = 'main'),
    url(r'^login/main/train/$', views.trainpage, name = 'train'),
    url(r'^main/encrypt/$', views.encrypt, name= 'encrypt'),
    url(r'^main/decryptpage/$', views.decryptpage, name= 'decryptpage'),
    url(r'^main/testpage/$', views.testpage, name= 'testpage'),


    
]