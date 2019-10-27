from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView,FormView
from django.http.response import HttpResponse

from accounts.models import User


from social_django.models import UserSocialAuth, AbstractUserSocialAuth
from social_django.utils import load_strategy
from . import forms

import spotipy

import requests
# Create your views here.

# class AddPlaylist(FormView):
#     form_class = forms.AddPlaylistForm
#     success_url = 'playlist_added'
#
#     def add_playlist(self, request):
#         return HttpResponse('Made it to the method')
#
#
#         # if request.method == 'post':
#         #     form = AddPlaylist.form_class(request.Post)
#         #     if form.is_valid():
#         #
#         #         user = User.objects.get('uid')
#         #         social = user.social_auth.get(provider='spotify')
#         #         token = social.extra_data['access_token']
#         #


class Test_Playlist(TemplateView):
    template_name = 'playlists/test_playlist.html'

class Playlist_Added(TemplateView):
    template_name = 'playlists/playlist_added.html'

def add_playlist(request):
    # return HttpResponse('This Worked')

    if request.user.is_authenticated:

        # user = User.objects.filter(id=2)

        # user = User.objects.get(id=2)

        user = request.user

        test = user.social_auth.get(provider='spotify')
        spotify_id = user.username
        token = test.extra_data['access_token']

        spotifyObject = spotipy.Spotify(auth=token)

        spotifyObject.user_playlist_create(user=spotify_id, name="Did it work, again?")

        new_playlist_json = spotifyObject.current_user_playlists(limit=1)

        new_playlist_id = new_playlist_json['items'][0]['id']

        track_list = ['54vEMXZQbeQ8ui3GKsKcnf', '11UK2krGqZXnr0khXrK7b6','547fOfZqXcCovdHNjywpEi']

        spotifyObject.user_playlist_add_tracks(user=spotify_id, playlist_id=new_playlist_id, tracks=track_list,
                                               position=None)


        return redirect("playlists:playlist_added")
    # if request.method == 'POST':


    else:
        return HttpResponse('Something did not work')