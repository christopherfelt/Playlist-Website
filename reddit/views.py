from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy, reverse

from . import forms
from . import models


import reddit.reddit


# Reddit Stuff
redditObject = reddit.reddit.RedditPlaylister()



# Create your views here.
# class SubredditPlaylist(FormView):
#
#     template_name = 'reddit/reddit_main.html'
#     form_class = forms.Subreddit
#     # success_url = reverse_lazy('reddit:reddit_home')
#
#     def form_valid(self, form):
#         subreddit = form.cleaned_data['subreddit']
#         return HttpResponse(subreddit)
class SubredditPlaylist(CreateView):

    template_name = 'reddit/reddit_main.html'
    form_class = forms.Subreddit_Form
    model = models.Subreddit
    # fields = ['subreddit', 'submission_type','spotify_id']# do not need these if using form class
    # success_url = reverse_lazy('reddit:subreddit_list')


    # def form_valid(self, form):
    #     subreddit = form.cleaned_data['subreddit']
    #     return HttpResponseRedirect(
    #         reverse('reddit:subreddit_list')
    #     )




    # def get_context_data(self, **kwargs):
    #     context = {'subreddit':self.subreddit}
    #     return context


class SubredditList(ListView):
    model = models.Subreddit
    template_name = "reddit/reddit_list.html"

    def get_queryset(self):
        subreddit_list = models.Subreddit.objects.filter(user='user.pk')
        return subreddit_list



    # def get_context_data(self, request, object_list=None, **kwargs):
    #     subreddit = kwargs['subreddit']
    #     subreddit_list = self.model.objects.filter(subreddit=subreddit)
    #     return subreddit_list




class RedditHome(TemplateView):

    template_name = "reddit/reddit_home.html"


# def subredditPlaylist(request):
