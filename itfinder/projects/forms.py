from django.forms import ModelForm
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'slug', 'tags',
                  'description', 'demo_link', 'source_link']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Оцените проект',
            'body': 'Добавьте комментарий'
        }