from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginView ,name='login'), 
    path('logout/', views.logoutView, name='logout'),
    # path('search/', views.search, name='search'),
    path('my/', views.CoursesListView, name='CourseList'),
    path('studentHome/', views.CoursesListView, name='StudentHome'),
    path('facultyCourses/', views.facultyCoursesView, name='facultyCourses'),    
    path('facultyHome/', views.facultyCoursesView, name='facultyHome'),    
    path('myProfile/<str:person_id>/', views.myProfileView, name='myProfile'),
    path('changeStudentPassword/', views.StudentPasswordView, name='changeStudentPassword'),    
    path('changeFacultyPassword/', views.FacultyPasswordView, name='changeFacultyPassword'), 
    path('facultyCoursePage/<str:course_id>/',views.FacultyCoursePageView,name='facultyCoursePage'),   
    path('Studentlist/<str:course_id>/',views.StudentListView,name='StudentList'),   
    path('studentCoursePage/<str:course_id>/',views.StudentCoursePageView,name='studentCoursePage'),   
]