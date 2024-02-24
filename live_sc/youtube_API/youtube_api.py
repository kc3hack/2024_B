from apiclient.discovery import build

videoId = 'hQtmJY84dNY'
YOUTUBE_API_KEY = 'AIzaSyAvV27NIXM5k4iAgGZH2wEI4qsNijbwZyE'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
videos_response = youtube.videos().list(
    part='snippet,statistics',
    id='{},'.format(videoId)
).execute()
# snippet
snippetInfo = videos_response["items"][0]["snippet"]
# 動画タイトル
title = snippetInfo['title']
# チャンネル名
channeltitle = snippetInfo['channelTitle']
print(channeltitle)
print(title)