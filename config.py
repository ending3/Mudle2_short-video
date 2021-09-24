import os

BASIC_PATH = os.path.dirname(os.path.abspath(__file__))
VIDEO_FILE_PATH = os.path.join(BASIC_PATH, 'db', 'video.csv')

NEWS_DICT = {}
with open(VIDEO_FILE_PATH, mode='r', encoding='utf-8')as file_object:
    for line in file_object:
        data = line.strip().split(',')
        news_id = data[0]
        news_title = data[1]
        news_url = data[-1]
        NEWS_DICT.setdefault(news_id, (news_title, news_url))


