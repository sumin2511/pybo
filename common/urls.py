from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from pybo.views import base_views

app_name = 'common'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', base_views.index, name='index'), #'/'에 해당되는 path
]