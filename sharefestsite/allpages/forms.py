from django import forms
from multi_email_field.forms import MultiEmailField

class SendMessageForm(forms.Form):
    emails = MultiEmailField()

class EmailForm(forms.Form):
    #Emails = forms.EmailField(required=False)
    #Emails = MultiEmailField(required=False)
    #Call the database and query all users 
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __str__(self):
        return self.Email
    