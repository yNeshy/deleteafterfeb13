from django.urls import path
from api import views

urlpatterns = [
    path("", views.endpoint, name="endpoint"),
    path("rules", views.rules, name="rules")
    
]