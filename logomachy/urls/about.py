from django.urls import path

from logomachy.views import about as about_views

app_name = 'logomachy'

urlpatterns = [
    path('terms/', about_views.TermsView.as_view(), name='terms'),
    path('privacy/', about_views.PrivacyView.as_view(), name='privacy'),
    path('credits/', about_views.CreditsView.as_view(), name='credits'),
]
