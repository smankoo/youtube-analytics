from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
# import pandas as pd
import pprint 
# import matplotlib.pyplot as pd
import json
import os

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

DEVELOPER_KEY = os.environ['GOOGLE_API_KEY']

def youtube_search(id=None):
    youtube_data = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    response = youtube.videos().list(
        part='statistics, snippet',
        id=id
    ).execute()

    for item in response['items']:

        channelId = item['snippet']['channelId']
        channelTitle = item['snippet']['channelTitle']
        title = item['snippet']['title']
        videoId = item['id']
        categoryId = item['snippet']['categoryId']
        publishedAt = item['snippet']['publishedAt']
        description = item['snippet']['description']
        favoriteCount = item['statistics']['favoriteCount']
        viewCount = item['statistics']['viewCount']
        likeCount = item['statistics']['likeCount']
        dislikeCount = item['statistics']['dislikeCount']

        # print(item)

        if 'commentCount' in item['statistics'].keys():
            commentCount = item['statistics']['commentCount']
        else:
            commentCount = ""
        
        if 'tags' in item['snippet'].keys():
            tags = item['snippet']['tags']
        else:
            tags = []
    #     pprint.pprint(response)
        item_dict = {'videoId':videoId,'channelId': channelId,'channelTitle': channelTitle,'tags':tags,'categoryId':categoryId,'title':title,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount, 'publishedAt':publishedAt, 'description':description}
        youtube_data.append(item_dict)

    return youtube_data


# youtube_search("Stephen Colbert")

# ids = [
# 'DFNvkfEC0xY',
# 'koJ-lmbdYLk'
# ]


def youtube_search_batch(ids, BATCH_SIZE=50):
    batch_ids = []
    prop = []
    batch_first = 0
    batch_last = 0
    batch_ids_string=""
    while True:
        # last batch will be smaller than others
        if(batch_last < len(ids)):
            batch_last = batch_last + BATCH_SIZE
        if(batch_last > len(ids)):
            batch_last = len(ids)

        # print("batch_last set to :"+str(batch_last))

        batch_ids = ids[batch_first:batch_last]
        batch_ids_string = ""
        for id in batch_ids:
            if(batch_ids_string == ""):
                batch_ids_string = batch_ids_string + id
            else:
                batch_ids_string = batch_ids_string + "," + id

        return youtube_search(batch_ids_string)
        
        # print("---------")

        batch_first = batch_first + BATCH_SIZE

        # if end of list has been reached, exit loop
        
        if(batch_last == len(ids) or batch_last > 50):
            break


# print(youtube_search2(ids=ids))
