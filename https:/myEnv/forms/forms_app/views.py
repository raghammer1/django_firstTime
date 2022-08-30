from django.shortcuts import render
from forms_app import forms

# Create your views here.
def index (request):
  return render(request, 'form_templates/index.html')

def form_name_view (request):
  form = forms.FormName()

  
  if request.method == 'POST':
    form = forms.FormName(request.POST)

    if form.is_valid():
      # Do something with the form data here
      print("Success")
      # here you pass the data you created in forms.py
      print("Name: "+form.cleaned_data['name'])
      print("Email: "+form.cleaned_data['email'])
      print("Email Re: "+form.cleaned_data['verify_email'])
      print("Says: "+form.cleaned_data['text'])

  return render(request, 'form_templates/forms_page.html', {'form': form})
