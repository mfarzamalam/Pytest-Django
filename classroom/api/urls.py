from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "api"


urlpatterns = [
    path('student/list/', StudentListApiView.as_view(), name='student_list_view'),
    path('student/create/', StudentCreateApiView.as_view(), name='student_create_view'),
    path('student/retrieve/<int:pk>/', StudentRetrieveApiView.as_view(), name='student_retrieve_view'),
    path('student/destroy/<int:pk>/', StudentDestroyApiView.as_view(), name='student_destroy_view'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/auth/', CheckAuthenticatedUser.as_view(), name='user_auth'),

]
