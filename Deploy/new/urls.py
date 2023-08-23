from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('predict/',views.predict_view,name='predict'),
    path('user_signup/',views.user_register,name='user_register'),
    path('signup/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('doctor_feedback/',views.feedback,name='feedback'),
    path('index/',views.apredict,name='apredict'),
    path('logout/',views.logout_view,name='logout'),
    path('last_patients/',views.view_last,name='details_last'),
    path('all_patients/',views.view_all,name='details_all'),
]
