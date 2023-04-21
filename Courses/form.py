from django.forms import ModelForm
from django import forms
from . models import Courses

from django.template.defaulttags import widthratio

class Courses_Form(ModelForm):
    class Meta:
        model = Courses
        fields = ('name', 'educator','description','excerpt','number_lessons','picture','video')
        widgets = {


            }

## chương trình up nhiều hình ảnh cùng lúc............................
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))