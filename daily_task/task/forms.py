from django import forms
from .models import Task

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'category')


class EditTaskForms(forms.Form):
    CATEGORY_OPTIONS = (
        ('urgent', 'Urgent'),
        ('important', 'Important'),
        ('needs_to_be_done', 'Needs to be done'),  
    )

    task = forms.CharField(max_length=400)
    category = forms.ChoiceField(choices=CATEGORY_OPTIONS)