from django.urls import path, include
from . import views

# If the user is on the main page, call the method from views.
urlpatterns = [
    path('', views.index)
]
