from urllib import response
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
        self.student_obj = mixer.blend(Student, first_name='Farzam')
        self.list_url = reverse('classroom:api:student_list_view')
        self.create_url = reverse('classroom:api:student_create_view')
        self.retrieve_url = reverse('classroom:api:student_retrieve_view', kwargs={'pk':1})
        self.destroy_url = reverse('classroom:api:student_destroy_view', kwargs={'pk':1})


    def test_list_view_pattern_url_is_equal_to_path_url(self):
        url = "/api/student/list/"
        assert self.list_url == url

    
    def test_create_view_pattern_url_is_equal_to_path_url(self):
        url = "/api/student/create/"
        assert self.create_url == url


    def test_retrieve_view_pattern_url_is_equal_to_path_url(self):
        url = "/api/student/retrieve/1/"
        assert self.retrieve_url == url


    def test_destroy_view_pattern_url_is_equal_to_path_url(self):
        url = "/api/student/destroy/1/"
        assert self.destroy_url == url


    def test_student_list_is_not_empty(self):
        response = self.client.get(self.list_url)
        assert response.status_code == 200
        assert len(response.json()) > 0


    def test_first_name(self):
        response = self.client.get(self.list_url)
        first_name = response.json()[0].get('first_name')

        assert response.status_code == 200
        assert first_name == "Farzam"


    def test_student_create_view(self):
        data = {
            "first_name": "asda",
            "last_name": "asd",
            "admission_number": 123,
            "is_qualified": True,
            "score": 123
        }
        response = self.client.post(self.create_url, data=data)
        assert response.status_code == 201


    def test_student_retrieve_view(self):
        response = self.client.get(self.retrieve_url)
        assert response.status_code == 200

    
    def test_student_delete_view(self):
        response = self.client.delete(self.destroy_url)
        assert response.status_code == 204