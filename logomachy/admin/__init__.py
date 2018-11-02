from django.contrib import admin
from logomachy import models as app_models

admin.site.register(app_models.Tag)
admin.site.register(app_models.Document)
admin.site.register(app_models.Revision)
admin.site.register(app_models.Result)
