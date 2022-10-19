from django.urls import path
from account.views import UserLoginView, UserProfileView, userRegistration, UserChangedPasswordView
urlpatterns = [

    path('register/', userRegistration.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('userprofile/', UserProfileView.as_view(), name='userprofile'),
    path('changePassword/', UserChangedPasswordView.as_view(), name='changePassword'),
]
