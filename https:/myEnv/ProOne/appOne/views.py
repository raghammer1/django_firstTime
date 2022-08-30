from django.shortcuts import render
from appOne.models import User

from appOne.forms import NewUserForm

# Create your views here.

def index(request):
  return render(request, 'appOne/index.html')

def users(request):
  form =  NewUserForm()

  if request.method == 'POST':
    form =  NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      print("succes")
      return index(request)
    else:
      print('Error form invalid')
  return render(request,'appOne/users.html', {'form': form})