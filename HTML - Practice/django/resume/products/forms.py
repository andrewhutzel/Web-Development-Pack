from django import forms
from .models import Feedback
from django.core.validators import MinValueValidator, MaxValueValidator
"""
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=30,required=True,error_messages={"required":"Please add your name."}, )
    rating = forms.IntegerField(min_value=1,max_value=5)
    text = forms.CharField(label="Your Feedback",max_length=256,widget=forms.Textarea)
    email = forms.EmailField()

"""

#Not sure how I want to flesh out this implementation.
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','rating','text',]
        labels = {'name':'Full Name','text':'Your Feedback'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].validators.append(MinValueValidator(1))
        self.fields['rating'].validators.append(MaxValueValidator(5))