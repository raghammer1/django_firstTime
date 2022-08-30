from django.db import models

# Create your models here.

class Topic(models.Model):
  top_name = models.CharField(max_length=264, unique=True)

  def __str__(self):
    return self.top_name
class Webpage(models.Model):
  # These are the fields that will be in the database
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  # maxlength is the maximum length allowed for the str to be
  name = models.CharField(max_length=148, unique=True)
  url = models.URLField(unique=True)

  def __str__(self):
    return self.name
  
class AccessRecord(models.Model):
  name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
  date = models.DateField()

  def __str__(self):
    return str(self.date)


########## After this you have to run in terminal ##########
# python manage.py migrate
# then
# python manage.py makemigrations app_name
# then run this again
# python manage.py migrate