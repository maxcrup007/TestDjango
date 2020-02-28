from django.forms import models
from .models import Question

class QuestionForm(models.ModelForm):
    class Meta:
        model = Question
        fields = ['title','description']
