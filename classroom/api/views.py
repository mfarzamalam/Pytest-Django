from webbrowser import get
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from classroom.api.serializers import StudentSerializer
from classroom.models import Student
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class CustomTokenObtainPairView(TokenObtainPairView):
    # permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer


class CheckAuthenticatedUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        return Response({
            'data':"OK"
        })

# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         response = {'status': True, 'message': 'User Logout Successfully'}

#         return Response(response, status=status.HTTP_200_OK)