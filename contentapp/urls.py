from django.urls import path
from . import views

app_name = "contentapp"

urlpatterns = [
    path('create_content/', views.CreateContentView.as_view(), name="create_content"),
    path('mypage/<str:username>/', views.MyPageView.as_view(), name="mypage"),
    path('typing_list/', views.TypingListView.as_view(), name="typing_list"),
]
