from rest_framework import viewsets, generics
from . import models, serializer

class StudentViewSet(viewsets.ModelViewSet):
    """"""
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """"""
    queryset = models.Course.objects.all()
    serializer_class = serializer.CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """"""
    queryset = models.Enrollment.objects.all()
    serializer_class = serializer.EnrollmentSerializer

class ListEnrollmentsStudent(generics.ListAPIView):
    """"""
    serializer_class = serializer.ListEnrollmentStudentSerializer
    def get_queryset(self):
        queryset = models.Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset

class ListofStudentsEnrolledInCourse(generics.ListAPIView):
    """"""
    serializer_class = serializer.ListofStudentsEnrolledInCourseSerializer
    def get_queryset(self):
        queryset = models.Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
