from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

def index(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dict = {'access_records':webpages_list}
  return render(request, 'first_app/index.html', context=date_dict)

def newIndex(request):
  return HttpResponse("<em>Hello, world!</em>")
  # Now we go to first_project/urls and add this view

def syna(request):
  my_dict = {'insert_me':"Now I am coming from views.py! And below is photo of my love Syna"}
  return render(request, 'first_app/index.html', context=my_dict)
  # Now we go to first_project/urls and add this view
