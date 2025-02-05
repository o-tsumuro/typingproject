from django.urls import path
from . import views

app_name = "typingapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.IndexView.as_view(), name='typing'),
    path('content_list/', views.ContentListView.as_view(), name="content_list"),
]
