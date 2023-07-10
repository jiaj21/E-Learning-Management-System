from django.forms import ModelForm
from django import forms
from Assignments.models import Assignments , Submission

# class AssignmentForm(ModelForm):
#     class Meta :
#         model = Assignments
#         fields=('assign_number', 'assign_title', 'question', 'assign_file', 'deadline')
#         widgets = {
#             'assign_number': forms.NumberInput(attrs={'class': 'form-control mt-3', 'name': 'assign_number','placeholder': 'Assignment Number'}),
            
#             'assign_title': forms.TextInput(attrs={'class': 'form-control mt-3', 'id': 'title', 'name': 'title', 'placeholder': 'Assignment Title'}),
            
#             'question': forms.TextInput(attrs={'class': 'form-control mt-3', 'id': 'title', 'name': 'Type', 'placeholder': 'Enter Question'}),
            
#             'deadline': forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'id': 'deadline', 'name': 'deadline', 'type': 'datetime-local'}),
            
#         }
        
# class AssignmentForm(forms.ModelForm):
#     class Meta:
#         model = Assignments
#         fields = ('assign_number', 'assign_title', 'question', 'deadline')
#         widgets = {
#             'assign_number': forms.NumberInput(attrs={'class': 'form-control mt-3', 'name': 'number', 'placeholder': 'Assignment Number'}),
#             'assign_title': forms.TextInput(attrs={'class': 'form-control mt-3', 'name': 'title', 'placeholder': 'Assignment Title'}),
#             'question': forms.TextInput(attrs={'class': 'form-control mt-3', 'name': 'question', 'placeholder': 'Enter Question'}),
#             # 'file': forms.ClearableFileInput(attrs={'class': 'mt-3', 'name': 'file'}),
#             'file' : forms.FileField(),
#             'deadline': forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'name': 'deadline', 'placeholder': 'Date Time' ,'type': 'datetime-local'})
#         }
        

class AssignmentForm(forms.Form):
    assign_number = forms.IntegerField(
        label='Assignment Number',
        widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'name': 'number', 'placeholder': 'Assignment Number'})
    )
    assign_title = forms.CharField(
        label='Assignment Title',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'name': 'title', 'placeholder': 'Assignment Title'})
    )
    question = forms.CharField(
        label='Question',
        widget=forms.Textarea(attrs={'class': 'form-control mt-3', 'name': 'question', 'placeholder': 'Enter Question'})
    )
    deadline = forms.DateTimeField(
        label='Deadline',
        widget=forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'name': 'deadline', 'placeholder': 'Date Time', 'type': 'datetime-local'})
    )
    file = forms.FileField(label='File')

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        # Add any file validation or custom logic here if required
        return file
