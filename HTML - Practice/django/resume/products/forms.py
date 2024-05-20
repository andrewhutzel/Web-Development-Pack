from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=30,required=True,error_messages={"required":"Please add your name."}, help_text="Add your name here, please.")
    rating = forms.IntegerField(min_value=1,max_value=10)
    text = forms.CharField(label="Your Feedback",max_length=256,widget=forms.Textarea)
    email = forms.EmailField()