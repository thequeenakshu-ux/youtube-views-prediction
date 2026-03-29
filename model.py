import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


df = pd.read_csv("youtube_data.csv")


df['views'] = df['views'].astype(int)
df['likes'] = df['likes'].astype(int)
df['comments'] = df['comments'].astype(int)


df['engagement_rate'] = (df['likes'] + df['comments']) / df['views']
df['title_length'] = df['title'].apply(len)


X = df[['likes', 'comments', 'engagement_rate', 'title_length']]


y = df['views']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = RandomForestRegressor()

model.fit(X_train, y_train)


predictions = model.predict(X_test)

print("Model trained successfully!")
print("Sample predictions:", predictions[:5])