from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school import views as school_view

router = routers.DefaultRouter()
router.register('students', school_view.StudentViewSet)
router.register('courses', school_view.CourseViewSet)
router.register('enrollments', school_view.EnrollmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments/', school_view.ListEnrollmentsStudent.as_view()),
    path('course/<int:pk>/enrollments/', school_view.ListofStudentsEnrolledInCourse.as_view()),
]
