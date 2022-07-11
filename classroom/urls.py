from django.urls import include, path

app_name = "classromm"

urlpatterns = [
    path('api/', include('classroom.api.urls'), name=''),
]
