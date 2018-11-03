"""logomachy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, re_path
from django.urls import path

sitemaps = {}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('', include('logomachy.urls'))
]

handler404 = 'logomachy.views.error_views.page_not_found_404'
handler500 = 'logomachy.views.error_views.server_error_500'
handler403 = 'logomachy.views.error_views.permission_denied_403'
handler400 = 'logomachy.views.error_views.bad_request_400'

if settings.DEBUG is True:
    # only provide direct access to static / media in development env
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    import debug_toolbar

    urlpatterns = [re_path(r'^__debug__/', include(debug_toolbar.urls))] + urlpatterns
