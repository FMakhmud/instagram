from django.urls import path
from core import urls
from instagram.views import CreateUserAPIView

urlpatterns = [
    path('user/create', CreateUserAPIView.as_view()),
    path('user/lohin', LoginAPIView.as_view()),
]
