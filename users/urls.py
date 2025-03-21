from django.urls import path
from .views import RegisterUserView, LoginUserView, UserListView, UserDetailView, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/', UserDetailView.as_view(), name='user-detail'),  # Add this line
     path('logout/', LogoutView.as_view(), name='logout'),
]