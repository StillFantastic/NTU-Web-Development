from django.urls import path
from .views import registration , registration_list

urlpatterns = [
    path('register/', registration, name='registration'),
    path('api/registration_list/', registration_list, name='registration_list'),
]
