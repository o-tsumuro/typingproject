from django.urls import path
from . import views

app_name = "contentapp"

urlpatterns = [
    path('create_content/', views.CreateContentView.as_view(), name="create_content"),
]
