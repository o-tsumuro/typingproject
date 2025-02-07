from django.urls import path
from . import views

app_name = "typingapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.IndexView.as_view(), name='typing'),

]
