from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('FacultyMaterialPage/<str:course_id>/',views.FacultyMaterialPageView,name='FacultyMaterialPage'), 
    path('StudentMaterialPage/<str:course_id>/',views.StudentMaterialPageView,name='StudentMaterialPage'), 
    path('AddMaterialPage/<str:course_id>/',views.AddMaterialPageView,name='AddMaterialPage'), 
    path('EditMaterial/<str:material_id>/<str:course_id>/',views.EditMaterialView,name='facultyEditMaterial'), 
    path('DeleteMaterial/<str:material_id>/<str:course_id>/',views.DeleteMaterialView,name='facultyDeleteMaterial'), 
     
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)