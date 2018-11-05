from django.urls import path

from logomachy.views import documents as doc_views
from logomachy.views import revisions as rev_views

app_name = 'logomachy'

urlpatterns = [
    path('', doc_views.IndexView.as_view(), name='index'),
    path('new/', doc_views.CreateView.as_view(), name='create'),
    path('<slug:name>/', doc_views.DetailView.as_view(), name='detail'),
    path('<slug:name>/modify/', doc_views.UpdateView.as_view(), name='update'),
    path('<slug:name>/revisions/new/', rev_views.CreateView.as_view(), name='revision_create'),
]
