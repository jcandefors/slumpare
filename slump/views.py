# Create your views here.
from django.db.models import Count
from slump.models import Dude, DTask, TaskForm
from django.shortcuts import render
from random import randint

def index(request):

   return render(request,'slump/index.html',{'form':TaskForm})

def result(request):
    if request.method == 'POST':
        tf = TaskForm(request.POST)
        if tf.is_valid():
            tdesc = tf.cleaned_data['desc']
            randomDude = Dude.objects.get(pk=randint(1,10))
            t = DTask(dude = randomDude, desc = tdesc)
            t.save()
            context = {'d_dude':randomDude , 'dtask' : tdesc}
            return render(request,'slump/random.html',context)
    else :
        form = TaskForm()

    return  render(request, 'slump/index.html', {'form': form,})



def history(request):
    tasks = DTask.objects.select_related().order_by('desc')
    # counts =DTask.objects.all().annotate('count' = Count('dude'))
    # return  render(request, 'slump/history.html', {'tasks': tasks,'counts':counts})
    return  render(request, 'slump/history.html', {'tasks': tasks})