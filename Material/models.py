from django.db import models
from main.models import Faculty , Course
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage

class CourseMaterial(models.Model) :
    material_number=models.IntegerField(primary_key=True)
    course_id= models.ForeignKey(
        Course, on_delete=models.CASCADE, null=False, related_name='Courses')
    faculty_id=models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name="Faculty")
    material_title=models.CharField(max_length = 200)
    file=models.FileField(upload_to="material/", null=False,blank=False)
    posted = models.DateTimeField(auto_now_add=True,editable=False, null=False)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.material_title
    
    class Meta:
        verbose_name_plural="Course Material"
        
@receiver(pre_delete, sender=CourseMaterial)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    # Delete the file if it exists
    if instance.file:
        default_storage.delete(instance.file.path)
@receiver(pre_save, sender=CourseMaterial)
def delete_file_on_field_update(sender, instance,**kwargs):
    try:
        # Get the initial instance from the database
        old_instance = CourseMaterial.objects.get(pk=instance.pk)
        if old_instance.file != instance.file :
            # Delete the old file if it exists
            if old_instance.file:
                default_storage.delete(old_instance.file.path)
    except:
        pass