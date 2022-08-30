from django.shortcuts import render

# Create your views here.

def index(request):
  mydict = {'newContent': 'Hello Help me please!'}
  return render(request, 'help.html', context=mydict)
