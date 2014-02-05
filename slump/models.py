from django.db import models
from django.forms import ModelForm
# Create your models here.

class Dude(models.Model):
    def __unicode__(self):
        return(self.name)

    name = models.CharField(max_length=40)
    nrOfTasks = models.IntegerField(default=0)

class DTask(models.Model):
    def __unicode__(self):
        return(self.desc)
    dude = models.ForeignKey(Dude)
    desc = models.CharField(max_length=200)

class TaskForm(ModelForm):
    class Meta:
        model = DTask
        fields = ['desc']
