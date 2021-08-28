from django.urls import path

from .views import HelloWorldView, DataView

urlpatterns = [
    path('world/', HelloWorldView.as_view()),
    path('data', DataView.as_view()),
]
