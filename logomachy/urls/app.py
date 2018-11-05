from django.urls import path, include
from logomachy import views as app_views

app_name = 'logomachy'

urlpatterns = [
    path('', app_views.IndexView.as_view(), name='home'),
    path('documents/', include('logomachy.urls.documents', namespace='documents')),
    path('revisions/', include('logomachy.urls.revisions', namespace='revisions')),
    path('tags/', include('logomachy.urls.tags', namespace='tags')),
    path('accounts/', include('logomachy.urls.accounts', namespace='accounts')),
    path('about/', include('logomachy.urls.about', namespace='about')),
]
