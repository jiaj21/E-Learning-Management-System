from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('FacultyAssignmentPage/<str:course_id>/',views.FacultyAssignmentPageView,name='FacultyAssignmentPage'),  
    path('CreateAssignmentPage/<str:course_id>/',views.CreateAssignmentPageView,name='CreateAssignmentPage'), 
    path('AboutAssignment/<str:assign_id>/',views.AboutAssignmentView,name='AboutAssignment'),
    path('EditAssignment/<str:assign_id>/',views.EditAssignmentView,name='facultyEditAssignment'),
    path('DeleteAssignment/<str:assign_id>/',views.DeleteAssignmentView,name='facultyDeleteAssignment'),
    path('studentAssignmentPage/<str:course_id>/',views.StudentAssignmentView,name='AssignmentList'),   
    path('studentAboutPage/<str:assign_id>/<str:student_id>/<str:course_id>/',views.StudentAboutAssignmentView,name='StudentAssignment'),   
    path('studentSubmissionPage/<str:assign_id>/<str:student_id>/<str:course_id>/',views.StudentSubmissionView,name='StudentSubmission'), 
    path('editSubmissionPage/<str:assign_id>/<str:student_id>/<str:course_id>/',views.EditSubmissionView,name='EditSubmission'), 
    path('deleteSubmissionPage/<str:assign_id>/<str:student_id>/<str:course_id>/',views.DeleteSubmissionView,name='DeleteSubmission'), 

]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)