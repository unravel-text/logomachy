from django.urls import path

from logomachy.views import tags as tag_views

app_name = 'logomachy'

urlpatterns = [
    path('', tag_views.IndexView.as_view(), name='index'),
    path('<slug:name>/', tag_views.DetailView.as_view(), name='detail'),
]
