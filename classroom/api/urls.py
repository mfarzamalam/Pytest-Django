from django.urls import path
from .views import *


urlpatterns = [
    path('student/', StudentListApiView.as_view(), name='studentAPI')
]
