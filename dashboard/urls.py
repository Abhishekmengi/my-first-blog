from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('business', views.business),
    path('newsconsumers', views.newsconsumers)
]