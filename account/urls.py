from django.urls import path
from account.views import userRegistration
urlpatterns = [

    path('register/', userRegistration.as_view(), name='register')
]
