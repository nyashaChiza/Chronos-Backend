
from django.contrib import admin
from django.urls import include
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url='/accounts/login/')),
    path("admin/", admin.site.urls),
    path("api/v1/accounts/", include('allauth.urls')),
    path("api/v1/", include('evaluation.urls')),
]


