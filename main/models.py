from django.db import models

# Create your models here.
# model for faculty
class Faculty(models.Model) :
    fac_id=models.IntegerField(primary_key=True)
    full_name=models.CharField(max_length=100,null=False)
    email_id=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=False)
    mobile_no=models.CharField(max_length=10,null=False)
    department=models.ForeignKey('Department',on_delete=models.CASCADE,null=False,related_name='faculty')

    class Meta:
        verbose_name_plural="Faculty"
    
    def __str__(self):
        return self.full_name
    
# model for departments
class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    department_name= models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.department_name

    def student_count(self):
        return self.students.count()

    def faculty_count(self):
        return self.faculty.count()

    def course_count(self):
        return self.courses.count()


# model for courses 
class Course(models.Model):
    course_code = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100, null=False, unique=True)
    department_name= models.ForeignKey(
        Department, on_delete=models.CASCADE, null=False, related_name='courses')
    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    studentKey = models.IntegerField(null=False, unique=True)
    facultyKey = models.IntegerField(null=False, unique=True)

    class Meta:
        unique_together = ('course_code', 'department_name', 'course_name')
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_name

class Student(models.Model) :
    stud_id=models.IntegerField(primary_key=True)
    full_name=models.CharField(max_length=100,null=False)
    email_id=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=False)
    mobile_no=models.CharField(max_length=10,null=False)
    department_name = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=False, blank=False, related_name='students')
    course_name = models.ManyToManyField(
        'Course', related_name='students', blank=True)
    
    class Meta:
        verbose_name_plural="Students"
        
    def __str__(self):
        return self.full_name
