from django.forms import ModelForm
from .models import Subreddit

# class Subreddit(forms.Form):
#     subreddit = forms.CharField()
#
#     class Meta:
#         fields = ('subreddit')
class Subreddit_Form(ModelForm):

    class Meta:
        model = Subreddit
        fields = ['subreddit','submission_type', 'spotify_id']

