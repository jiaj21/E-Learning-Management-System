from django.shortcuts import render,redirect
from main.models import Student , Faculty , Course , Department
from Assignments.models import Assignments
from django.contrib import messages
from django.db.models import Count
from django.template.defaulttags import register
from django.http import HttpResponse


def loginView(request):
    if request.method=="POST":
        id=request.POST['ID']
        password=request.POST['password']
        
        if Student.objects.filter(stud_id=id,password=password).exists():
            request.session['stud_id']=id
            return redirect('/my/') 
        
        elif Faculty.objects.filter(fac_id=id,password=password).exists():
            request.session['fac_id']=id
            return redirect('/facultyCourses/') 
        
        else:
            messages.error(request,("Invalid Login Credentials"))
    
    
    return render(request,'login.html')

def logoutView(request):
    request.session.flush()
    return redirect('login')



def CoursesListView(request):
    if request.session['stud_id']:
            student = Student.objects.get(
                stud_id=request.session['stud_id'])
            courses = student.course_name.all().values()
            id=Faculty.objects.values_list('fac_id')
            name=Faculty.objects.values_list('full_name')
            dict={}
            index=0
            for i in id:
                dict[int(i[0])]=str(name[index][0])
                index+=1
            
            @register.filter
            def get_item(dictionary, id):
                return dictionary.get(id)
            data = {
                'courses': courses,
                'student': student,
                'dict': dict
            }
            

    return render(request, 'CourseList.html',data)


def facultyCoursesView(request):
    if request.session['fac_id']:
            faculty = Faculty.objects.get(
                fac_id=request.session['fac_id'])
            courses = Course.objects.filter(
                faculty_id=request.session['fac_id'])
            studentCount = Course.objects.all().annotate(student_count=Count('students'))

            dict = {}

            for i in studentCount:
                dict[i.course_code] = i.student_count
            
            @register.filter
            def get_item(dictionary, course_code):
                return dictionary.get(course_code)
            
            data = {
                'courses': courses,
                'faculty': faculty,
                'dict': dict
            }    
            

    return render(request, 'FacultyCourseList.html',data)

def myProfileView(request,person_id):
    try: 
        if request.session['stud_id']==person_id:
            student=Student.objects.get(stud_id=person_id)
            dict={'student':student}
            return render(request,'StudentProfile.html',dict)
    except:
        if request.session['fac_id']==person_id:
            faculty=Faculty.objects.get(fac_id=person_id)
            dict={'faculty':faculty}
            # return render(request,'FacultyProfile.html',dict)
            return render(request,'FacultyProfile.html',dict) 

        
def StudentPasswordView(request):
    if request.method=="POST":
        old_pass=request.POST['old']
        new_pass=request.POST['new']
        confirm_pass=request.POST['confirm']
        student=Student.objects.get(stud_id=request.session['stud_id'])
        if student.password==old_pass:
            if new_pass==confirm_pass:
                student.password=new_pass
                student.save()
                messages.success(request,('Password Saved Successfully'))
                return redirect('login')
            else:
                messages.success(request,("New password and old password not same"))
                return redirect('login')
        else:
            messages.success(request,("Wrong password entered"))
            return redirect('login')
    
    
    return render(request,'StudentPassword.html')


def FacultyPasswordView(request):
    if request.method=="POST":
        old_pass=request.POST['old']
        new_pass=request.POST['new']
        confirm_pass=request.POST['confirm']
        faculty=Faculty.objects.get(fac_id=request.session['fac_id'])
        if faculty.password==old_pass:
            if new_pass==confirm_pass:
                faculty.password=new_pass
                faculty.save()
                messages.success(request,('Password Saved Successfully'))
                return redirect('login')
            else:
                messages.success(request,("New password and old password not same"))
                return redirect('login')
        else:
            messages.success(request,("Wrong password entered"))
            return redirect('login')
    
    
    return render(request,'FacultyPassword.html')


def FacultyCoursePageView(request,course_id):
    if request.session['fac_id']:
        courses = Course.objects.get(
                course_code=course_id)
        faculty = Faculty.objects.get(
                fac_id=request.session['fac_id'])
        assign=Assignments.objects.filter(course_code=course_id)
        # disscuss=Discussion.objects.filter(course_code=course_id)
        # material=Course_Material.objects.filter(course_code=course_id)
        
        data={
            'courses': courses,
            'assign':assign,
            'faculty':faculty
        }
        return render(request,'faculty_course_page.html',data)
    
def StudentCoursePageView(request,course_id):
    if request.session['stud_id']:
        courses = Course.objects.get(
                course_code=course_id)
        student = Student.objects.get(
                stud_id=request.session['stud_id'])
        assign=Assignments.objects.filter(course_code=course_id)
        # disscuss=Discussion.objects.filter(course_code=course_id)
        # material=Course_Material.objects.filter(course_code=course_id)
        
        data={
            'courses': courses,
            'assign':assign,
            'student':student
        }
        return render(request,'StudentCoursePage.html',data)

def StudentListView(request,course_id):
    if request.session['fac_id']:
        courses = Course.objects.get(
                course_code=course_id)
        faculty = Faculty.objects.get(
                fac_id=request.session['fac_id'])
        try: 
            student=Student.objects.filter(course_name=course_id)
        except Student.DoesNotExist:
            student=None
        student_count=student.count()
        data={
            'courses':courses,
            'faculty':faculty,
            'student':student,
            'student_count':student_count
        }
        return render(request,'StudentList.html',data)
        
        
        


        
