from django.urls import path

from . import views

urlpatterns = [
    path('', views.email_generator),
    path('<int:amount>', views.email_generator)
]
