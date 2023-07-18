from django import forms
from .models import *


class PlayListForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=30)
    image_playlist = forms.FileField(required=True)


class SongForm(forms.Form):

    name_song = forms.CharField(max_length=30)
    mp3 = forms.FileField()
    background = forms.FileField()
    playlist_id = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user
        print(self.user)
        choices = PlayList.objects.values_list('id', 'title').filter(user_id=self.user.id)
        self.fields['playlist_id'].choices = choices
