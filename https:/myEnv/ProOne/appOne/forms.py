from django import forms
from appOne.models import User

class NewUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = '__all__'
    # fields = ['first_name', 'last_name', 'email']