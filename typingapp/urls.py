from django.urls import path
from . import views

app_name = "typingapp"

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
]
