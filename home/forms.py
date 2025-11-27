from django import forms
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.Form):

    captcha = ReCaptchaField()

    CHOICES = (('1', 'Choose Structure'), ('2', 'Sunroom'),
               ('3', 'Retractable Pergola'), ('4', 'Louvered Roof'))


    name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={'id': 'contact-name', 'name': 'contact-name', 'required': 'required', 'placeholder':'Your Name *'}))

    email = forms.EmailField(max_length=120, widget=forms.EmailInput(
        attrs={'id': 'contact-email', 'name': 'contact-email', 'required': 'required', 'placeholder':'Email Address*' }))

    phone = forms.CharField(max_length=12, required=False,
                            widget=forms.TextInput(attrs={'id': 'contact-phone', 'name': 'contact-phone', 'placeholder':'Your Phone'}))

    structure = forms.ChoiceField(choices=CHOICES)

    message = forms.CharField(max_length=2000, widget=forms.Textarea(
        attrs={'id': 'contact-message', 'name': 'contact-message', 'required': 'required', 'placeholder':'Message*'}))
















