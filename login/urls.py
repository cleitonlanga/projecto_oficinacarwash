from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.sigin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
]
