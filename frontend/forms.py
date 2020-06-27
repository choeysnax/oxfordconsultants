from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, widget=forms.Textarea())
    email = forms.EmailField()
    phone = forms.CharField(max_length=500, widget=forms.Textarea())
    subject = forms.CharField(max_length=500, widget=forms.Textarea())
    message = forms.CharField(max_length=500, widget=forms.Textarea())
