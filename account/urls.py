from django.urls import path, include

from account.views import *

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),

]