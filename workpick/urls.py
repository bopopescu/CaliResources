from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^register/',user_views.register,name='register'),
    path(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path(r'^profile/' ,user_views.profile ,name='profile'),
    path(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('',include('blog.urls')),
    path(r'^password-reset/',
    auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
     path(r'^password-reset-done/',
    auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
      path(r'^password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
     path(r'^password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
