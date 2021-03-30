from django.urls import path
from .views import SignUpUserView, DisplayUserView, UpdateUserView, DeleteUserView, PasswordUserChangeView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('display/<int:pk>', DisplayUserView.as_view(), name='display'),
    path('update/<int:pk>', UpdateUserView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteUserView.as_view(), name='delete'),
    path('password/', PasswordUserChangeView.as_view(), name='change_password')
]