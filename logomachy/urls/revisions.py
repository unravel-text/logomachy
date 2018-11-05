from django.urls import path

from logomachy.views import revisions as rev_views

app_name = 'logomachy'

urlpatterns = [
    path('', rev_views.IndexView.as_view(), name='index'),
    path('<uuid:name>/', rev_views.DetailView.as_view(), name='detail'),
]
