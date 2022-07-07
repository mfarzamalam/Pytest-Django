from unittest import TestCase
from classroom.models import Student


class TestStudentModel(TestCase):
    def setUp(self):
        self.student_obj = Student.objects.create(first_name='farzam', last_name='alam',
        is_qualified=True, score=200)
    
    def test_a_plus_b_is_equal_to_c(self):
        print("\ntest_a_plus_b_is_equal_to_c")
        a = 10
        b = 10
        c = 20
        self.assertEqual(a+b, c)

    def test_first_name_comma_last_name(self):
        print("\ntest_first_name_comma_last_name")
        expected_name = "%s, %s" %("farzam", "alam")
        self.assertEqual(str(self.student_obj), expected_name)

    def test_admission_number_is_greater_than_5_digit(self):
        print("\ntest_admission_number_is_greater_than_5_digit")
        self.student_obj.admission_number = 2000
        self.student_obj.save()
        self.assertEquals(len(str(self.student_obj.admission_number)), 5)

    def tearDown(self):
        Student.objects.all().delete()