from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
  return render(request, "basic_app/index.html")

# we need to add this decorator here so that django automatically checks if a user is logged in or not else we would just be logginh out
# un logged in users
@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

@login_required
def special(required):
  HttpResponse("succesfully logged out")

def register(request):
  registered = False

  if request.method == "POST":
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileInfoForm(data=request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      # saving user to database
      user = user_form.save()
      # taking user password from database and hashing it
      user.set_password(user.password)
      # saving the changes to user again
      user.save()

      profile = profile_form.save(commit=False) 
      # THis below line is finally where we are using that OneToOneField that we created in model.py 
      profile.user = user

      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']
      
      profile.save()

      registered = True

    else:
      print(user_form.errors, profile_form.errors)

  else:
    user_form = UserForm()
    profile_form = UserProfileInfoForm()

  # in the return dictionary we need to pass all the things we are using in the html that corresponds to this view

  return render(request, "basic_app/registration.html", {
    "user_form": user_form,
    "profile_form": profile_form,
    "registered": registered,
  })


def user_login(request):
  if request.method == "POST":
    # you can pass in get the names of input that you used in the html tha corresponds to this view
    username = request.POST.get('username')
    password = request.POST.get('password')

    # This will automatically authenticate the user for us
    user = authenticate(username=username, password=password)

    if user:
      if user.is_active:
        login(request=request, user=user)
        return HttpResponseRedirect(reverse('index'))

      return HttpResponse("Account not Active")

    return HttpResponse("Account does not exist 2")

  return render(request, 'basic_app/login.html', {})