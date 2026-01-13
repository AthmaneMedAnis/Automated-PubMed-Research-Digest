from wordcloud import WordCloud
from os import path

import matplotlib.pyplot as plt
import pandas as pd

def generate_wordcloud(abstract_text:pd.Series, output_path:str):
    """
    Generates and saves a word cloud image from a pandas Series of text.
    """
    text_data = [str(t) for t in abstract_text if t and str(t).lower() != 'nan']
    combined_text = " ".join(text_data)
    
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=100
    ).generate(combined_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()