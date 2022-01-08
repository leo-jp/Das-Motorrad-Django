from django.urls import path

from . import views

urlpatterns = [
    path('', views.companies),
    path('<int:company>', views.company)
]