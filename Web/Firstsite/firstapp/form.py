from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class createProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "name..."}))
    manHour = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "manHour..."}))
    prework = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "prework..."}))