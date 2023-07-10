from django.shortcuts import render,redirect
from main.models import Student , Faculty , Course , Department
from Material.models import CourseMaterial
from django.contrib import messages
from Material.forms import MaterialForm 

def FacultyMaterialPageView(request,course_id):
    courses = Course.objects.get(
                course_code=course_id)
    faculty = Faculty.objects.get(
                fac_id=request.session['fac_id'])
    material=CourseMaterial.objects.filter(course_id=course_id)
    data={
            'courses': courses,
            'material':material,
            'faculty':faculty
        }
    return render(request,'FacultyMaterialPage.html',data)

def AddMaterialPageView(request,course_id):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            number = form.cleaned_data['material_number']
            title = form.cleaned_data['material_title']
            myfile = form.cleaned_data['file']
            description = form.cleaned_data['description']
            c_code= Course.objects.get(course_code=course_id)
            f_id= Faculty.objects.get(fac_id=request.session['fac_id'])

            new_material=CourseMaterial()
            new_material.material_number=number
            new_material.material_title=title
            new_material.course_id=c_code
            new_material.faculty_id=f_id
            new_material.file=myfile
            new_material.description=description
            new_material.save()
            messages.success(request,("Assignmnet Saved Successfully"))

            return redirect('/FacultyMaterialPage/'+ str(course_id))  
        else:
                errors = form.errors
                for field, error_list in errors.items():
                    for error in error_list:
                        print(f"Error in field '{field}': {error}")  
                        messages.success(request,("Couldn't Add Material. Form Is Not Valid"))
    else:
        form = MaterialForm()
    
    course=Course.objects.get(course_code=course_id)
    faculty=Faculty.objects.get(fac_id=request.session['fac_id'])
    data={
                'course':course,
                'faculty':faculty,
                'forms':form
            }
    return render(request,'AddMaterial.html',data)

def DeleteMaterialView(request,material_id,course_id):
    if request.session['fac_id']:
        material=CourseMaterial.objects.get(material_number=material_id)
        material.delete()
        return redirect('/FacultyMaterialPage/'+ str(course_id))

def EditMaterialView(request,material_id,course_id):
    if request.session['fac_id']:
        if request.method=='POST' or request.method=='FILES':
            material=CourseMaterial.objects.get(material_number=material_id)
            if request.POST['Material Title']:
                material.material_title=request.POST['Material Title']
            try:
                request.FILES['File']
                material.file=request.FILES['File']
            except:
                pass
            material.save()
            return redirect('/FacultyMaterialPage/'+ str(course_id))
    course=Course.objects.get(course_code=course_id)
    faculty=Faculty.objects.get(fac_id=request.session['fac_id'])
    material=CourseMaterial.objects.get(material_number=material_id)
    data={
            'courses': course,
            'material':material,
            'faculty':faculty
        }
    return render(request,'FacultyEditMaterial.html',data)

def StudentMaterialPageView(request,course_id):
    if request.session['stud_id']:
        courses = Course.objects.get(course_code=course_id)
        student = Student.objects.get(stud_id=request.session['stud_id'])
        material=CourseMaterial.objects.filter(course_id=course_id)
    data={
            'courses': courses,
            'material':material,
            'student':student
        }
    return render(request,'StudentMaterialPage.html',data)

