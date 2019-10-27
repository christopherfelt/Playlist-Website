import praw
import requests
import re
import spotipy
import spotipy.util as util
from pprint import pprint
import credentials

reddit_client_id = credentials.reddit_client_id
reddit_client_secret = credentials.reddit_client_secret
reddit_reddit_name = credentials.reddit_name

reddit = praw.Reddit(client_id = reddit_client_id, client_secret=reddit_client_secret, user_agent = 'me')

subreddit = reddit.subreddit('listentothis')

topten = subreddit.hot(limit=100)

token = util.oauth2.SpotifyClientCredentials()

cache_token = token.get_access_token()

spotify = spotipy.Spotify(cache_token)

artist = ""
search_string = ""
search_list = {}
search_material = {}

youtube_count = 0
spotify_count = 0
bandcamp_count = 0
other_count = 0

for thing in topten:
    try:
        test_string = thing.title

        pattern = "(.*?)\-."
        artist = re.search(pattern, test_string).group(1)
        artist = artist.strip()


        song_patterns = [".\-+(.*?)(\(|\[).", ".\-+(.*)"]
        song = ""

        for pattern in song_patterns:
            try:
                song = re.search(pattern, test_string).group(1)
                song = song.strip()
                break
            except:
                pass


        url_thing = thing.url
        search_string = song

        if "youtube" in url_thing or "youtu.be" in url_thing:
            url_item = "youtube"
            youtube_count = youtube_count + 1
        elif "spotify" in url_thing:
            url_item = "spotify"
            spotify_count = spotify_count + 1
        elif "bandcamp" in url_thing:
            url_item = "bandcamp"
            bandcamp_count = bandcamp_count + 1
        else:
            url_item = url_thing
            other_count = other_count + 1



        print(test_string," | ", artist, " | ", song.strip(), " | ", search_string, " | ",  url_thing)
        print()

        # search_list.append(search_string)

        search_list[search_string] = artist

        search_material[search_string] = [url_item]


    except Exception as e:
        print ('*****ERROR*****', thing.title, e)

print('youtube: ', youtube_count)
print('spotify: ', spotify_count)
print('bandcamp: ', bandcamp_count)
print('other: ', other_count)

success_count = 0
success_list = {}
reject = True
reject_list = {}

search_list = {}
search_list['Continental Drift'] = 'Virus'

print_list = ['None']

for search in search_list:

    results = spotify.search(q=search, type='track', limit=50)
    if search in print_list or print_list[0] == 'all':
        print('------------')
        # print(results)
    try:
        item_count = len(results['tracks']['items'])
        for i in range(0, item_count):
            if reject == False:
                reject = True
                break

            name = results['tracks']['items'][i]['album']['artists'][0]['name']
            things = results['tracks']['items'][i]['name']
            thing_id = results['tracks']['items'][i]['id']
            if name.lower()== search_list[search].lower() and things.lower() == search.lower():

                if search in print_list or print_list[0]=='all':
                    print('Reddit Artist: ', search_list[search])
                    print('Reddit Song: ', search)
                    print('---Artist: ',name)
                    print('---Track Name: ',things)
                    print('---Track ID: ', thing_id)
                    print()
                success_count = success_count+1
                success_list[things] = name
                reject = False

            elif name.lower()==search.lower() and things.lower() == search_list[search].lower():

                if search in print_list or print_list[0] == 'all':
                    print('Reddit Artist: ', search_list[search])
                    print('Reddit Song: ', search)
                    print('---Artist: ',name)
                    print('---Track Name: ',things)
                    print('---Track ID: ', thing_id)
                    print()
                success_count = success_count+1
                success_list[name] = things
                reject = False
            else:
                if search in print_list or print_list[0] == 'all':
                    print('Reject')
                    print('Reddit Artist: ', search_list[search])
                    print('Reddit Song: ', search)
                    print('---Artist: ',name)
                    print('---Track Name: ',things)
                    print('---Track ID: ', thing_id)
                    print()


    except:
        print("issue")
        print(len(results['tracks']['items']))

    if reject == True:
        reject_list[search] = search_list[search]
    else:
        reject = True

print('Rejected')
reject_match = False
reject_fix_count = 0
reject_fix_list = {}
reject_fix_print_list = ['Continental Drift']
for rejected in reject_list:
    results = spotify.search(q=reject_list[rejected]+"NOT*", type='artist', limit=50)
    print(results)

    if rejected in reject_fix_print_list or reject_fix_print_list[0]=='all':
        print('Track: ', rejected, '| Artist: ', reject_list[rejected])

    if len(results['artists']['items']) > 0:
        for k in range(0, len(results['artists']['items'])):
            reject_artist = results['artists']['items'][k]['name']
            print("reject artist: ", reject_artist)
            if reject_artist.lower() == reject_list[rejected].lower():
                track_results = spotify.search(q="artist:"+reject_artist, type='album')
                if rejected in reject_fix_print_list or reject_fix_print_list[0] == 'all':
                    print(reject_artist, ' == ', reject_list[rejected])
                for i in range (0,len(track_results['albums']['items'])):
                    if reject_match == True:
                        reject_match = False
                        break
                    album_id = track_results['albums']['items'][i]['id']
                    album_name = track_results['albums']['items'][i]['name']
                    album_tracks = spotify.album_tracks(album_id)
                    if rejected in reject_fix_print_list or reject_fix_print_list[0] == 'all':
                        print('album: ',album_name)
                        print('tracks')
                    for j in range(0, len(album_tracks['items'])):
                        track_name = album_tracks['items'][j]['name']
                        if rejected in reject_fix_print_list or reject_fix_print_list[0] == 'all':
                            print('- ', track_name)
                        if track_name.lower() == rejected.lower():
                            if rejected in reject_fix_print_list or reject_fix_print_list[0] == 'all':
                                print("-- Match")
                            reject_fix_list[track_name] = reject_artist
                            reject_match = True
                            reject_fix_count = reject_fix_count + 1

print()
print('Searchable Items: ', len(search_list))
for search in search_list:
    print('\t', search, " - ", search_list[search])

print('Success: ', success_count)
for success in success_list:
    print('\t', success, " - ", success_list[success])


print('Initial Rejects: ', len(reject_list))
reject_print_list = ['Tour CD']
for reject in reject_list:
    print('\t', reject, " - ", reject_list[reject])
    if reject.lower() in reject_print_list:
        print('\t\t', "URL Type: ", search_material[reject])
print('Reject Fixes: ', reject_fix_count)
for fix in reject_fix_list:
    print('\t', fix, " - ", reject_fix_list[fix])




# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print (artist)