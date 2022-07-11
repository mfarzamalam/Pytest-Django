import pytest 
from classroom.models import Student
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse


pytestmark = pytest.mark.django_db


class StudentApiTestView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = mixer.blend(Student, first_name='Farzam')
        self.url = reverse('classroom:api:student_list_view')


    def test_pattern_url_is_equal_to_path_url(self):
        url = "/api/student/list/"
        assert self.url == url


    def test_student_list_is_not_empty(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert len(response.json()) > 0


    def test_first_name(self):
        response = self.client.get(self.url)
        first_name = response.json()[0].get('first_name')

        assert response.status_code == 200
        assert first_name == "Farzam"
