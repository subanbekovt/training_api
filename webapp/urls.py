from django.urls import path

from webapp.views import get_csrf_token_view

urlpatterns = [
    path("", get_csrf_token_view),
]
