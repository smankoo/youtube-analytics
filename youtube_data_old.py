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


    channelId         = []
    channelTitle      = []
    title             = []
    videoId           = []
    categoryId        = []
    publishedAt       = []
    description       = []
    favoriteCount     = []
    viewCount        = []
    likeCount         = []
    dislikeCount      = []
    commentCount    = []
    tags            = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    response = youtube.videos().list(
        part='statistics, snippet',
        id=id
    ).execute()

    for item in response['items']:

        channelId.append(item['snippet']['channelId'])
        channelTitle.append(item['snippet']['channelTitle'])
        title.append(item['snippet']['title'])
        videoId.append(item['id'])
        categoryId.append(item['snippet']['categoryId'])
        publishedAt.append(item['snippet']['publishedAt'])
        description.append(item['snippet']['description'])
        favoriteCount.append(item['statistics']['favoriteCount'])
        viewCount.append(item['statistics']['viewCount'])
        likeCount.append(item['statistics']['likeCount'])
        dislikeCount.append(item['statistics']['dislikeCount'])

        # print(item)

        if 'commentCount' in item['statistics'].keys():
            commentCount.append(item['statistics']['commentCount'])
        else:
            commentCount.append("")
        
        if 'tags' in item['snippet'].keys():
            tags.append(item['snippet']['tags'])
        else:
            tags.append([])
    #     pprint.pprint(response)
    youtube_dict = {'videoId':videoId,'channelId': channelId,'channelTitle': channelTitle,'tags':tags,'categoryId':categoryId,'title':title,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount, 'publishedAt':publishedAt, 'description':description}

    return youtube_dict


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
