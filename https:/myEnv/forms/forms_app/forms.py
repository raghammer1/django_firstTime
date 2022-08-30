import email
from wsgiref.validate import validator
from django import forms
from django.core import validators

# Now to make your own custom validators do this these self created ones also are included in the validators array down in the botcatcher field
def check_for_s(value):
  if value[0].lower() != 's':
    raise forms.ValidationError('Name needs to start with a s')



class FormName(forms.Form):
  name = forms.CharField(max_length=100, validators=[check_for_s])
  email = forms.EmailField(max_length=200)
  verify_email = forms.EmailField(max_length=200, label="Please enter your email address again")
  text = forms.CharField(widget = forms.Textarea)
  # hidden fields are hidden for users but catch bots
  # what bot will do is that instead of actually filling the form it will try and fill the html
  # where it will  also try to fill the botcatcher field and hence we can catch it there
  
  botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

  # ONE WAY TO CATCH THE BOT else the easy way is to just add a validator field and then pass a array of validators to the botcatcher and catch the bot
  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if len(botcatcher) > 0:
  #     raise forms.ValidationError("Caught the bot")
    
  #   return botcatcher

  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    verify_email = all_clean_data['verify_email']

    if email != verify_email:
      raise forms.ValidationError("Email and verify_email don't match")
    
  