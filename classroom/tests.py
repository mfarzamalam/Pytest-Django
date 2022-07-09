# from unittest import TestCase
from classroom.models import ClassRoom, Student
import pytest
from mixer.backend.django import mixer
from hypothesis import strategies, given
from hypothesis.extra.django import TestCase


pytestmark = pytest.mark.django_db


class TestStudentModel(TestCase):
    def setUp(self):
        self.student_obj = Student.objects.create(first_name='farzam', last_name='alam',
        is_qualified=True, score=80)
    
    def test_a_plus_b_is_equal_to_c(self):
        # print("\ntest_a_plus_b_is_equal_to_c")
        a = 10
        b = 10
        c = 20
        # self.assertEqual(a+b, c)
        assert a+b == c


    def test_first_name_comma_last_name(self):
        expected_name = "%s, %s" %("farzam", "alam")
        # self.assertEqual(str(self.student_obj), expected_name)
        assert str(self.student_obj) == expected_name


    @given(strategies.integers(min_value=10000, max_value=10000000))
    def test_admission_number_is_greater_than_4_digit(self, random_value):
        print("random_value", random_value)
        self.student_obj.admission_number = random_value
        self.student_obj.save()
        # self.assertEqual(len(str(self.student_obj.admission_number)), 5)
        assert len(str(self.student_obj.admission_number)) > 4


    @given(strategies.integers(min_value=30, max_value=59))
    def test_student_is_passed(self, random_value):
        print("random_value", random_value)
        self.student_obj.score = random_value
        self.student_obj.save()
        # self.assertEqual(self.student_obj.get_score_grade(), "Promoted")
        assert self.student_obj.get_score_grade() == "Passed"


    @given(strategies.integers(min_value=0, max_value=29))
    def test_student_is_failed(self, random_value):
        print("random_value", random_value)
        self.student_obj.score = random_value
        self.student_obj.save()
        # self.assertEqual(self.student_obj.get_score_grade(), "Failed")
        assert self.student_obj.get_score_grade() == "Failed"


    @given(strategies.integers(min_value=60, max_value=100))
    def test_student_is_promoted(self, random_value):
        print("random_value", random_value)
        self.student_obj.score = random_value
        self.student_obj.save()
        # self.assertEqual(self.student_obj.get_score_grade(), "Promoted")
        assert self.student_obj.get_score_grade() == "Promoted"


    @given(strategies.integers(min_value=101, max_value=1000))
    def test_student_score_has_incorrect_value(self, random_value):
        print("random_value", random_value)
        self.student_obj.score = random_value
        self.student_obj.save()
        # self.assertEqual(self.student_obj.get_score_grade(), "Score should be in the range of 0-100")
        assert self.student_obj.get_score_grade() == "Score should be in the range of 0-100"
    
    # def tearDown(self):
    #     Student.objects.all().delete()


class TestClassRoom(TestCase):
    def test_physics_classroom_has_been_created(self):
        classroom_obj = mixer.blend(ClassRoom, name='Physics')
        assert str(classroom_obj) == "Physics"