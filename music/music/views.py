from django.shortcuts import render, redirect
from playlist.models import Song, PlayList
from django.db.models import Q


def home(request):
    userid = request.user.id
    your_playlist = PlayList.objects.all().filter(user_id=userid).order_by('-id')[0:3]
    other_playlist = PlayList.objects.all().filter(~Q(user_id=userid)).order_by('-id')[0:4]
    data = {'one': your_playlist, 'two': other_playlist}
    return render(request, template_name='home.html', context=data)
