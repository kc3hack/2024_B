from ast import keyword
from apiclient.discovery import build

keyword = '大阪工業大学'
YOUTUBE_API_KEY = 'AIzaSyAvV27NIXM5k4iAgGZH2wEI4qsNijbwZyE'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
search_responses = youtube.search().list(
    q=keyword,
    part='snippet',
    type='video',
    regionCode="jp",
    maxResults=5,# 5~50まで
).execute()
for search_response in search_responses['items']:
    # snippet
    snippetInfo = search_response['snippet']
    # 動画タイトル
    title = snippetInfo['title']
    # チャンネル名
    channeltitle = snippetInfo['channelTitle']
    print(channeltitle)
    print(title)