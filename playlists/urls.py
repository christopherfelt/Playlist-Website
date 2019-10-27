from django.urls import path
from . import views

app_name = 'playlists'

urlpatterns = [
    # path('add_playlist/', views.AddPlaylist.as_view(), name='add_playlist'),
    path('test_playlist/', views.Test_Playlist.as_view(), name='test_playlist'),
    path('playlist_added/', views.Playlist_Added.as_view(), name='playlist_added'),
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    # path('add_playlist2/', views.AddPlaylist.as_view(), 'add_playlist2')
]