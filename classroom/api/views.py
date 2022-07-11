from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from classroom.api.serializers import StudentSerializer
from classroom.models import Student


class StudentListApiView(ListAPIView):
    serializer_class = StudentSerializer
    # permission_classes = []
    queryset = Student.objects.all()


class StudentCreateApiView(CreateAPIView):
    serializer_class = StudentSerializer
    # permission_classes = []
    queryset = Student.objects.all()


class StudentDestroyApiView(DestroyAPIView):
    serializer_class = StudentSerializer
    # permission_classes = []
    queryset = Student.objects.all()


class StudentRetrieveApiView(RetrieveAPIView):
    serializer_class = StudentSerializer
    # permission_classes = []
    queryset = Student.objects.all()