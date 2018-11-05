from django.urls import path

from logomachy.views import accounts as acc_views

app_name = 'logomachy'

urlpatterns = [
    path('', acc_views.IndexView.as_view(), name='index'),
    path('profile/<username>', acc_views.ProfileView.as_view(), name='profile'),
    path('profile/', acc_views.ProfileView.as_view(), name='profile_current'),
    path('login/', acc_views.LoginView.as_view(), name='login'),
    path('logout/', acc_views.LogoutView.as_view(), name='logout'),
    path('password_change/', acc_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', acc_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', acc_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', acc_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', acc_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', acc_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]