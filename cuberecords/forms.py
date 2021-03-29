from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    email = forms.EmailField(label='E-Mail', max_length=128)
    password = forms.CharField(label='Password', min_length=3, max_length=128,
                               widget=forms.PasswordInput)
    password_again = forms.CharField(label='Password, again', min_length=3, max_length=128,
                                     widget=forms.PasswordInput)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)


class RecordRequestForm(forms.Form):
    description = forms.CharField(label='Description', max_length=64)
    spent_time = forms.FloatField()
    #document = forms.FileField()
