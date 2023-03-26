from django.shortcuts import render, redirect
from .models import Music
from .forms import MusicForm
# Create your views here.
def index(request):
    musics = Music.objects.all()
    context = {
        "musics":musics,
    }
    return render(request, 'music/index.html', context)

def detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    context =  {
       "music": music,
    }
    return render(request, 'music/detail.html', context)

def create(request):
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save()
            return redirect('music:detail', music.pk)
    else:
        form = MusicForm()
    context = {
        "form":form
        }
    return render(request, 'music/create.html', context)