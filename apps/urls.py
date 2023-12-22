from django.urls import path, include

urlpatterns = [
    path('', include("django_reg.urls")),
    path('contact/', include('contact.urls'))
]