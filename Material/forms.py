from django import forms


class MaterialForm(forms.Form):
    material_number = forms.IntegerField(
        label='Material Number',
        widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'name': 'number', 'placeholder': 'Material Number'})
    )
    material_title = forms.CharField(
        label='Material Title',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'name': 'title', 'placeholder': 'Material Title'})
    )
    file = forms.FileField(label='File')
    description=forms.CharField(
        label='description',
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control mt-3', 'name': 'description', 'placeholder': 'about this material'})
    )

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        # Add any file validation or custom logic here if required
        return file