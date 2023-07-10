from django.shortcuts import render,redirect
from main.models import Student , Faculty , Course , Department
from Assignments.models import Assignments,Submission
from django.contrib import messages
from django.db.models import Count
from django.template.defaulttags import register
from Assignments.forms import AssignmentForm 
from datetime import datetime
from django.utils import timezone

def FacultyAssignmentPageView(request,course_id):
    courses = Course.objects.get(
                course_code=course_id)
    faculty = Faculty.objects.get(
                fac_id=request.session['fac_id'])
    assign=Assignments.objects.filter(course_code=course_id)
    data={
            'courses': courses,
            'assign':assign,
            'faculty':faculty
        }
    return render(request,'FacultyAssignmentPage.html',data)



def CreateAssignmentPageView(request,course_id):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            number = form.cleaned_data['assign_number']
            title = form.cleaned_data['assign_title']
            question = form.cleaned_data['question']
            deadline = form.cleaned_data['deadline']
            myfile = form.cleaned_data['file']
            c_code= Course.objects.get(course_code=course_id)
            f_id= Faculty.objects.get(fac_id=request.session['fac_id'])

            new_assignment=Assignments()
            new_assignment.assign_number=number
            new_assignment.assign_title=title
            new_assignment.question=question
            new_assignment.deadline=deadline
            new_assignment.course_code=c_code
            new_assignment.fac_id=f_id
            new_assignment.file=myfile
            new_assignment.save()
            messages.success(request,("Assignmnet Saved Successfully"))

            return redirect('/FacultyAssignmentPage/'+ str(course_id))  # Redirect to a success page after saving
        else:
                errors = form.errors
                for field, error_list in errors.items():
                    for error in error_list:
                        print(f"Error in field '{field}': {error}")  
                        messages.success(request,("Couldn't Create Assignment. Form Is Not Valid"))
    else:
        form = AssignmentForm()
    
    course=Course.objects.get(course_code=course_id)
    faculty=Faculty.objects.get(fac_id=request.session['fac_id'])
    data={
                'course':course,
                'faculty':faculty,
                'forms':form
            }
    return render(request,'CreateAssignment.html',data)

def AboutAssignmentView(request,assign_id):
    if request.session['fac_id']:
        assign=Assignments.objects.get(assign_number=assign_id)
        faculty=Faculty.objects.get(fac_id=request.session['fac_id'])
        # course=Course.objects.get(course_code=course_id)
        try: 
            submission=Submission.objects.filter(assignment=assign_id)
        except Submission.DoesNotExist:
            submission=None
        total_count=(Student.objects.filter(course_name=assign.course_code)).count()
        submitted_count=(submission).count()
        data={
            'assign':assign,
            'faculty':faculty,
            'submission':submission,
            'total_count':total_count,
            'submitted_count':submitted_count
            }
        return render(request,'FacultyAboutAssignment.html',data)
    
def EditAssignmentView(request,assign_id):
    if request.session['fac_id']:
        if request.method=='POST':
            assignment=Assignments.objects.get(assign_number=request.POST['Assignment Number'])
            if request.POST['Assignment Title']:
                assignment.assign_title=request.POST['Assignment Title']
            if request.POST['Question']:
                assignment.question=request.POST['Question']
            try: 
                request.FILES['File']
                assignment.file=request.FILES['File']
            except:
                pass
            if request.POST['deadline']:
                assignment.deadline=request.POST['deadline']
            assignment.save()
            return redirect('/AboutAssignment/'+ str(assign_id))
    assign=Assignments.objects.get(assign_number=assign_id)
    faculty=Faculty.objects.get(fac_id=request.session['fac_id'])
    data={
            'assign':assign,
            'faculty':faculty
            }
    return render(request,'FacultyEditAssignment.html',data)

def DeleteAssignmentView(request,assign_id):
    if request.session['fac_id']:
        assignment=Assignments.objects.get(assign_number=assign_id)
        course_id=assignment.course_code.course_code
        assignment.delete()
    return redirect('/FacultyAssignmentPage/'+ str(course_id))

def StudentAssignmentView(request,course_id):
    if request.session['stud_id']:
        courses = Course.objects.get(course_code=course_id)
        student = Student.objects.get(stud_id=request.session['stud_id'])
        assign=Assignments.objects.filter(course_code=course_id)
    data={
            'courses': courses,
            'assign':assign,
            'student':student
        }
    return render(request,'StudentAssignmentPage.html',data)

def StudentAboutAssignmentView(request,assign_id,student_id,course_id):
    if request.session['stud_id']:
        courses = Course.objects.get(course_code=course_id)
        assign=Assignments.objects.get(assign_number=assign_id)
        student=Student.objects.get(stud_id=student_id)
        try: 
            submission=Submission.objects.get(assignment=assign_id ,student_code=student_id)
            current_time=submission.submitted_time
            time_diff=assign.deadline-current_time
            days=abs(time_diff.days)
            hours=abs(time_diff.seconds//3600)
            if time_diff.total_seconds() < 0:
                due=0
            else:
                due=1
        except Submission.DoesNotExist:
            submission=None
            current_time=timezone.now()
            time_diff=assign.deadline-current_time
            days=abs(time_diff.days)
            hours=abs(time_diff.seconds//3600)
            if time_diff.total_seconds() < 0:
                due=0
            else:
                due=1
                
            
    data={
        'assign':assign,
        'student':student,
        'submission':submission,
        'courses':courses,
        'due':due,
        'days':days,
        'hours':hours
        }
    return render(request,'StudentAboutAssignment.html',data)

def StudentSubmissionView(request,assign_id,student_id,course_id):
    if request.session['stud_id']:
        if request.method=='POST':
            submission=Submission()
            if request.FILES['File']:
                submission.submission_file=request.FILES['File']
                submission.assignment=Assignments.objects.get(assign_number=assign_id)
                submission.course_id=Course.objects.get(course_code=course_id)
                submission.student_code=Student.objects.get(stud_id=student_id)
                fac=Course.objects.get(course_code=course_id)
                submission.fac_id=fac.faculty
                submission.save()
                return redirect('/studentAboutPage/'+ str(assign_id)+'/'+str(student_id)+'/'+str(course_id))
    student=Student.objects.get(stud_id=student_id)
    course=Course.objects.get(course_code=course_id)
    assign=Assignments.objects.get(assign_number=assign_id)
    data={
        'student':student,
        'courses':course,
        'assign':assign
    }
    return render(request,'StudentSubmission.html',data)


def EditSubmissionView(request,assign_id,student_id,course_id):
    if request.session['stud_id']:
        if request.method=='POST':
            if request.FILES['File']:
                submission=Submission.objects.get(assignment=assign_id ,student_code=student_id)
                submission.submission_file=request.FILES['File']
                submission.submitted_time = timezone.now()
                submission.save()
                return redirect('/studentAboutPage/'+ str(assign_id)+'/'+str(student_id)+'/'+str(course_id))
    student=Student.objects.get(stud_id=student_id)
    course=Course.objects.get(course_code=course_id)
    assign=Assignments.objects.get(assign_number=assign_id)
    data={
        'student':student,
        'courses':course,
        'assign':assign
    }
    return render(request,'StudentSubmission.html',data)

def DeleteSubmissionView(request,assign_id,student_id,course_id):
    if request.session['stud_id']:
        submission=Submission.objects.get(assignment=assign_id ,student_code=student_id)
        submission.delete()
        return redirect('/studentAboutPage/'+ str(assign_id)+'/'+str(student_id)+'/'+str(course_id))
    
                
            
        
        
        
        
    
    
            
            
        
        

  
           
    
    
    