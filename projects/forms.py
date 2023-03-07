from django.forms import ModelForm
from projects.models import Project


ClassProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "owner"]
