from django.urls import path,include 
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .forms import *



urlpatterns = [
    path('', views.home, name='home'),
    path('video/<int:video_id>/', views.watch_video, name='watch_video'),
    path('video/add_comment/', views.add_comment, name='add_comment'),
    path('video/add_like/<int:video_id>/', views.add_like, name='add_like'),
    path('<str:session_username>/profile/', views.profile, name='profile'),
    path('<str:session_username>/dashboard/', views.dashboard, name='dashboard'),
    path('add_subscriber/<viewer>/', views.add_sub, name='add_subscriber'),
    path('upload/', views.upload_video, name='upload'), 
    path('edit_video/<int:video_id>', views.edit_video, name='edit_video'),
    path('delete_video/', views.delete_video, name='delete_video'),
    path('update_details/', views.update_details, name='update_details'),
    path('signup/', views.signup, name='signup'),   
    path('login/', views.user_login, name='login'),  
    path('logout/', views.user_logout, name='logout'),  

    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/password_reset/confirm/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/password_reset/confirm/validate_token/', include('django_rest_passwordreset.urls', namespace='password_reset')),

  

    path('search/', views.search, name='search'),   
    path('change-password/', PasswordChangeView.as_view(template_name='change-password.html', form_class=Changepasswordform), name='change-password'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),  
    path('change', views.password,name='change'),

    path('passwordreset/', PasswordResetView.as_view(template_name='passwordreset.html', form_class=PasswordResetForm), name='passwordreset'), 
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='passwodConfirmation.html', form_class=PasswordResetConfirm), name='password_reset_confirm'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='passwordResetDone.html'), name="password_reset_done"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='passwordSuccessful.html'), name="password_reset_complete"), 
    
]       