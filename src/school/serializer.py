from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = models.Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = models.Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = models.Enrollment
        fields = '__all__'

class ListEnrollmentStudentSerializer(serializers.ModelSerializer):
    """"""
    course = serializers.ReadOnlyField(source='course.description')
    time_course = serializers.SerializerMethodField()

    class Meta:
        model = models.Enrollment
        fields = ['course', 'time_course']

    def get_time_course(self, obj):
        return obj.get_time_course_display()

class ListofStudentsEnrolledInCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = models.Enrollment
        fields = ['student_name']
