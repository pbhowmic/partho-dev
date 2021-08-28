from django.urls import path

from .views import HellowWorldView, DataView

urlpatterns = [
    path('world/', HellowWorldView.as_view()),
    path('data', DataView.as_view()),
]
