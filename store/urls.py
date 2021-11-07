from django.urls import path
from .views import login,signup,home

urlpatterns = [
    #path('',index,name = 'homepage'),
    # path('signup',signup),
    # path('login',login),
    #path('',home.index,name = 'home'),
    path('',home.Index.as_view(),name = 'home'),
    path('login',login.Login.as_view(),name = 'login'),
    path('signup',signup.Signup.as_view(),name = 'signup'),
]
