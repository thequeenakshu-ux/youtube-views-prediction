from googleapiclient.discovery import build
import pandas as pd


API_KEY = "AIzaSyAOznFute0V2MwunQjRaSa7l6hDx6RJM0k"


youtube = build('youtube', 'v3', developerKey=API_KEY)


search_req = youtube.search().list(
    part="snippet",
    q="machine learning",
    type="video",
    maxResults=20
)

search_res = search_req.execute()

video_list = []

print("Getting video basic details...")

for i in search_res['items']:
    vid = i['id']['videoId']
    title = i['snippet']['title']
    channel = i['snippet']['channelTitle']
    date = i['snippet']['publishedAt']

    video_list.append([vid, title, channel, date])


df = pd.DataFrame(video_list, columns=["video_id", "title", "channel", "published"])


ids = ",".join(df['video_id'])

print("Now fetching statistics...")

stats_req = youtube.videos().list(
    part="statistics",
    id=ids
)

stats_res = stats_req.execute()

view_list = []
like_list = []
comment_list = []


for j in stats_res['items']:
    stats = j['statistics']

    
    view_list.append(stats.get('viewCount', 0))
    like_list.append(stats.get('likeCount', 0))
    comment_list.append(stats.get('commentCount', 0))


df['views'] = view_list
df['likes'] = like_list
df['comments'] = comment_list


df.to_csv("youtube_data.csv", index=False)

print("Done 👍 data saved!")