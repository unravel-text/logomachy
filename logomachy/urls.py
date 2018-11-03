from django.urls import path, include
from logomachy import views as app_views
from logomachy.views import accounts as acc_views
from logomachy.views import documents as doc_views
from logomachy.views import revisions as rev_views
from logomachy.views import tags as tag_views
from logomachy.views import about as about_views

documents_urlpatterns = [
    path('', doc_views.IndexView.as_view(), name='documents_index'),
    path('new/', doc_views.CreateView.as_view(), name='documents_create'),
    path('<slug:name>/', doc_views.DetailView.as_view(), name='documents_detail'),
    path('<slug:name>/modify/', doc_views.UpdateView.as_view(), name='documents_update'),
    path('<slug:name>/revision/new/', rev_views.CreateView.as_view(), name='revisions_create'),
]

revisions_urlpatterns = [
    path('', rev_views.IndexView.as_view(), name='revisions_index'),
    path('<uuid:name>/', rev_views.DetailView.as_view(), name='revisions_detail'),
]

tags_urlpatterns = [
    path('', tag_views.IndexView.as_view(), name='tags_index'),
    path('<slug:name>/', tag_views.DetailView.as_view(), name='tags_detail'),
]

accounts_urlpatterns = [
    path('', acc_views.IndexView.as_view(), name='accounts_index'),
    path('profile/<username>', acc_views.ProfileView.as_view(), name='accounts_profile'),
    path('profile/', acc_views.ProfileView.as_view(), name='accounts_profile_current'),
    path('login/', acc_views.LoginView.as_view(), name='accounts_login'),
    path('logout/', acc_views.LogoutView.as_view(), name='accounts_logout'),

    path('password_change/', acc_views.PasswordChangeView.as_view(), name='accounts_password_change'),
    path('password_change/done/', acc_views.PasswordChangeDoneView.as_view(), name='accounts_password_change_done'),

    path('password_reset/', acc_views.PasswordResetView.as_view(), name='accounts_password_reset'),
    path('password_reset/done/', acc_views.PasswordResetDoneView.as_view(), name='accounts_password_reset_done'),
    path('reset/<uidb64>/<token>/', acc_views.PasswordResetConfirmView.as_view(),
         name='accounts_password_reset_confirm'),
    path('reset/done/', acc_views.PasswordResetCompleteView.as_view(), name='accounts_password_reset_complete'),
]

about_urlpatterns = [
    path('terms/', about_views.TermsView.as_view(), name='about_terms'),
    path('privacy/', about_views.PrivacyView.as_view(), name='about_privacy'),
    path('credits/', about_views.CreditsView.as_view(), name='about_credits'),
]

urlpatterns = [
    path('', app_views.IndexView.as_view(), name='home'),
    path('documents/', include(documents_urlpatterns), name='documents'),
    path('revisions/', include(revisions_urlpatterns), name='revisions'),
    path('tags/', include(tags_urlpatterns), name='tags'),
    path('accounts/', include(accounts_urlpatterns), name='accounts'),
    path('about/', include(about_urlpatterns), name='about'),
]


