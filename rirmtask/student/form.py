from django import forms

class student_data(forms.Form):
    roll_number = forms.CharField(max_length=5)
    name = forms.CharField(max_length=20)
    student_class = forms.CharField(max_length = 10)
    school_name = forms.CharField(max_length = 10)
    mobile = forms.CharField(max_length=10)
    address = forms.CharField(max_length=50)

class studentacademics_data(forms.Form):
    id = forms.CharField()
    roll_number = forms.CharField()
    maths = forms.CharField(max_length=10)
    physics = forms.CharField(max_length=10)
    chemistry = forms.CharField(max_length=10)
    biology = forms.CharField(max_length=10)
    english = forms.CharField(max_length=10)