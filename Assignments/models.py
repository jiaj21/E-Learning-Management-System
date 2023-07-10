from django.db import models

from main.models import Student , Faculty , Course , Department
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage

class Assignments(models.Model) :
    assign_number=models.IntegerField(primary_key=True,default=0)
    course_code= models.ForeignKey(
        Course, on_delete=models.CASCADE, null=False, related_name='course')
    fac_id=models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name="faculty")
    assign_title=models.CharField(max_length = 200)
    question = models.TextField(max_length = 1000)
    file=models.FileField(upload_to="question/", null=True,default=None,blank=True)
    created = models.DateTimeField(auto_now_add=True,editable=False, null=False)
    deadline = models.DateTimeField(null=False,editable=True)
    
    def __str__(self):
        return self.assign_title
    
    class Meta:
        verbose_name_plural="Assignments"
        
@receiver(pre_delete, sender=Assignments)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    # Delete the file if it exists
    if instance.file:
        default_storage.delete(instance.file.path)
@receiver(pre_save, sender=Assignments)
def delete_file_on_field_update(sender, instance,**kwargs):
    try:
        # Get the initial instance from the database
        old_instance = Assignments.objects.get(pk=instance.pk)
        if old_instance.file != instance.file :
            # Delete the old file if it exists
            if old_instance.file:
                default_storage.delete(old_instance.file.path)
    except:
        pass

   
        
        
class Submission(models.Model) :
    assignment=models.ForeignKey(Assignments, on_delete=models.CASCADE, null=False, related_name='assg_number')
    course_id= models.ForeignKey(
        Course, on_delete=models.CASCADE, null=False, related_name='courses')
    student_code=models.ForeignKey(
        Student, on_delete=models.SET_NULL, related_name="student",null=True)
    fac_id=models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name="fac")
    submission_file=models.FileField(upload_to="submissions/",max_length=250, null=True,default=None)
    submitted_time= models.DateTimeField(auto_now_add=True,editable=False, null=False)
    
    class Meta:
        verbose_name_plural="Submission"
        
    def __str__(self):
        return self.student_code.full_name
    
@receiver(pre_delete, sender=Submission)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    # Delete the file if it exists
    if instance.submission_file:
        default_storage.delete(instance.submission_file.path)
@receiver(pre_save, sender=Submission)
def delete_file_on_field_update(sender, instance,**kwargs):
    try:
        # Get the initial instance from the database
        old_instance = Submission.objects.get(pk=instance.pk)
        if old_instance.submission_file != instance.submission_file :
            # Delete the old file if it exists
            if old_instance.submission_file:
                default_storage.delete(old_instance.submission_file.path)
    except:
        pass
    
