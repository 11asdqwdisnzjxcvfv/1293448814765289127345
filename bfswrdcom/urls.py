from django.urls import path

from index.views import IndexHTML

urlpatterns = [
    path('', IndexHTML.as_view()),
]
