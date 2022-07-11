from rest_framework.serializers import ModelSerializer
from classroom.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'admission_number', 'is_qualified', 'score')

    # def to_representation(self, instance):
    #     data = super(StudentSerializer, self).to_representation(instance)
    #     # manipulate data here 
    #     return data
