from django.urls import path

import reddit.views as views

app_name = "reddit"

urlpatterns = [

    path('main/', views.SubredditPlaylist.as_view(), name = 'reddit_main'),
    path('home/', views.RedditHome.as_view(), name='reddit_home'),
    path('subreddit_list/', views.SubredditList.as_view(), name='subreddit_list')

]