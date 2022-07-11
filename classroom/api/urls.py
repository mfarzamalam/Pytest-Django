from django.urls import path
from .views import *


app_name = "api"


urlpatterns = [
    path('student/list/', StudentListApiView.as_view(), name='student_list_view'),
    path('student/create/', StudentCreateApiView.as_view(), name='student_create_view'),
    path('student/retrieve/<int:pk>/', StudentRetrieveApiView.as_view(), name='student_retrieve_view'),
    path('student/destroy/<int:pk>/', StudentDestroyApiView.as_view(), name='student_destroy_view'),
]
