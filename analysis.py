import pandas as pd


df = pd.read_csv("youtube_data.csv")


print(df.head())


print(df.info())


print(df.describe())


df['views'] = df['views'].astype(int)
df['likes'] = df['likes'].astype(int)
df['comments'] = df['comments'].astype(int)


df['published'] = pd.to_datetime(df['published'])


df.dropna(inplace=True)

print("Data cleaned")


df['views'] = df['views'].astype(int)
df['likes'] = df['likes'].astype(int)
df['comments'] = df['comments'].astype(int)


df['published'] = pd.to_datetime(df['published'])


df.dropna(inplace=True)

print("Data cleaned")


top_videos = df.sort_values(by='views', ascending=False).head(5)

print(top_videos[['title', 'views']])


df['engagement_rate'] = (df['likes'] + df['comments']) / df['views']

print("\nEngagement Rate Added:")
print(df[['views', 'likes', 'comments', 'engagement_rate']].head())

top_engagement = df.sort_values(by='engagement_rate', ascending=False).head(5)

print("\nTop Engaging Videos:")
print(top_engagement[['title', 'engagement_rate']])

df['like_to_view_ratio'] = df['likes'] / df['views']

print(df.isnull().sum())
