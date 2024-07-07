from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=(('m','Male'),('f','Female')))
    