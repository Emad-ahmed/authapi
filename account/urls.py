from django.urls import path
from account.views import UserLoginView, userRegistration
urlpatterns = [

    path('register/', userRegistration.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]
