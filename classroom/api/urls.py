from django.urls import path
from .views import *

app_name = "api"

urlpatterns = [
    path('student/', StudentListApiView.as_view(), name='student_list_view')
]
