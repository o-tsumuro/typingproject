from django.urls import path
from . import views

app_name = "typingapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.TypingView.as_view(), name='typing'),
    path('result/<int:pk>/<int:typing_time>/', views.ResultView.as_view(), name='result'),
    path('guest_result/<int:pk>/<int:typing_time>', views.GuestResultView.as_view(), name='guest_result'),
]
