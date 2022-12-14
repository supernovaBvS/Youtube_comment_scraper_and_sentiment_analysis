
from youtube_comment_scraper_python import *
import pandas as pd

def utube():
    link = input("Youtube links: ")
    file = input("file name: ")
    youtube.open(link)

    response = youtube.video_comments()
    data = response['body']

    df = pd.DataFrame(data)

    return df
# df.to_csv(file)