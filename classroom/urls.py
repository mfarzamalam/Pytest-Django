from django.urls import include, path

app_name = "classroom"

urlpatterns = [
    path('api/', include('classroom.api.urls')),
]
