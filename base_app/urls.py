from django.conf.urls import url
from base_app import views

app_name = 'base_app'
urlpatterns = [
    # url(r'^login/$', views.loginView.as_view(), name = 'login'),
    # url(r'^register/$', views.RegisterView.as_view(), name = 'register'),
    url(r'^login/$', views.userlogin, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/main/$', views.mainpage, name = 'main'),
    url(r'^login/main/train/$', views.trainpage, name = 'train')
    # url(r'^decrypt/$', views.decryptPageView.as_view(), name = 'decrypt'),
    # url(r'^train/(?P<pk>\d+)$', views.trainImageView.as_view(), name = 'train'),

]