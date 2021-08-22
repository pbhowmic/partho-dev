from django.urls import path

from .views import HellowWorldView

urlpatterns = [
    path('world/', HellowWorldView.as_view()),
]
