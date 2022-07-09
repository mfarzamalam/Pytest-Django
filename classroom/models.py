from django.db import models
from django.core.exceptions import ValidationError


def negative_error(value):
    if value < 0:
        raise ValidationError("%s is not a postive integer" %(value))

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    admission_number = models.IntegerField(null=True, blank=True)
    is_qualified = models.BooleanField(default=False)
    score = models.IntegerField(validators=[negative_error])

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    def get_score_grade(self):
        if self.score < 0 or self.score > 100:
            return "Score should be in the range of 0-100"
        elif self.score < 30:
            return "Failed"
        elif self.score >= 30 and self.score < 60:
            return "Passed"
        elif self.score >= 60 and self.score <= 100:
            return "Promoted"

    class Meta:
        db_table = u"student"


class ClassRoom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = u"classroom"