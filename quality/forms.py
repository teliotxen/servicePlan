from django import forms
from .models import Projects, Scenario, Block, Comments, Review



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'desc', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5']


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ['title', 'desc', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5']


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = ['desc']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['desc', 'status', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['desc', 'status', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5']
