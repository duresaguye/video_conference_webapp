from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'password_mismatch': 'The two password fields didn’t match.',
            'password_too_similar': 'Your password is too similar to your other personal information.',
            'password_too_short': 'Your password must contain at least 8 characters.',
            'password_too_common': 'Your password is too common.',
            'password_entirely_numeric': 'Your password can’t be entirely numeric.',
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user