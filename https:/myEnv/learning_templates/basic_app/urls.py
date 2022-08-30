from django.urls import path, include
from basic_app import views

# This keyword needs to match in our html code to build a relative path to this file
app_name = 'basic_app'

urlpatterns = [
  path('other/', views.other, name='other'),
  path('relative/', views.relative_url_templates, name='relative'),
]