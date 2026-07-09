from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your name"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Enter a valid 10-digit phone number."
            )
        ],
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter phone number"
        })
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject"
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Write your message"
        })
    )


class RegisterForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your E-Mail"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Password"
        })
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"
        })
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )

    terms = forms.BooleanField(
        required=True,
        error_messages={
            "required": "You must agree to the Terms and Privacy Policy."
        }
    )

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(username=email).exists():
            raise ValidationError("Email already registered.")

        return email