from rest_framework.generics import ListAPIView
from classroom.api.serializers import StudentSerializer
from classroom.models import Student


class StudentListApiView(ListAPIView):
    serializer_class = StudentSerializer
    # permission_classes = []
    queryset = Student.objects.all()