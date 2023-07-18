from django.shortcuts import render, redirect
from .models import Song, PlayList
from .forms import PlayListForm, SongForm


def choose(request):
    if request.user.is_authenticated:
        userid = request.user.id
        songList = Song.objects.filter(user_id=userid)
        playlistList = PlayList.objects.filter(user_id=userid)
        data = {'one': userid, 'two': songList, 'three': playlistList}
        return render(request, template_name='playlist/choose_add.html', context=data)
    else:
        return render(request, template_name='playlist/choose_add.html')


def playlist(request):
    if request.method == 'POST':
        form = PlayListForm(request.POST)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            return redirect('choose')
    else:
        form = PlayListForm()
    return render(request, template_name='playlist/playlist_add.html', context={'form': form})


def song(request):
    if request.method == 'POST':
        return redirect('choose')
    else:
        form = SongForm(user=request.user)
        return render(request, template_name='playlist/song_add.html', context={'form': form})
