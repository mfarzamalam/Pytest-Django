from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    admission_number = models.IntegerField()
    is_qualified = models.BooleanField(default=False)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.is_qualified}"

    def get_score_grade(self):
        if self.score < 30:
            return "Failed"
        elif self.score > 30 and self.score < 60:
            return "Passed"
        elif self.score > 60:
            return "Pormoted"

    class Meta:
        db_table = u"student"


class ClassRoom(models.Model):
    name = models.CharField(max_length=256)
    i_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = u"classroom"