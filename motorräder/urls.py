from django.urls import path

from . import views

urlpatterns = [
    path('', views.MotorräderView.as_view()),
    path('<int:company>', views.MotorradView.as_view())
]