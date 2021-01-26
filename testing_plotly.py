import pandas as pd
import plotly.express as px

# data = {
#     'positive': [1],
#     'negative': [4],
#     'neutral': [7],
#     'date': ['jan-1']
# }

data = {
    'sentiscore': [4],
    'date': ['jan-1']
}

df = pd.DataFrame(data, columns=['sentiscore', 'date'])

print(df)

fig = px.bar(data, x='date', y='sentiscore', title='Ocular Sentiment Analysis Library Chart')
fig.show()