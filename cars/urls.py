
from django.urls import path
from cars import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cars, name="cars" ),
] 