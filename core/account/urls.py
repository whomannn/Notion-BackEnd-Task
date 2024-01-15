from django.urls import include,path
from .views import RegisterUserView

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("register/",RegisterUserView.as_view(),name='register')
]




