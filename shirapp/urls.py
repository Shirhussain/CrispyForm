from django.urls import path, include
from .views import index, senippet_detail

urlpatterns = [
    path('', index, name = "index"),
    path('sneppit/',senippet_detail, name = "sneppit"),
]
