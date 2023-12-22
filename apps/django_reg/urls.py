from django.urls import path
from .views import SignUpView, indexView

urlpatterns = [
    path('', indexView, name='index'),
    path('signup/', SignUpView.as_view(), name='register'),
]