import pandas as pd
import plotly.express as px

data = {
    'positive': [1, 2, 3],
    'negative': [4, 5, 6],
    'neutral': [7, 8, 9],
}

df = pd.DataFrame(data, columns=['positive', 'negative', 'neutral'])

fig = px.bar(data, x='soren', y='negative', title='Ocular Sentiment Analysis Library Chart')
fig.show()