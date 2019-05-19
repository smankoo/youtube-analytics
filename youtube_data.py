from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint 
import matplotlib.pyplot as pd
import json


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

with open ('credentials.json', 'rb') as jsonfile:
    credentials = json.load(jsonfile)

DEVELOPER_KEY = credentials['GOOGLE_API_KEY']

# def youtube_search(id=None):

#     youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

#     response = youtube.videos().list(
#         part='statistics, snippet',
#         id=id
#     ).execute()

#     channelId = response['items'][0]['snippet']['channelId']
#     channelTitle = response['items'][0]['snippet']['channelTitle']
#     title = response['items'][0]['snippet']['title']
#     videoId = response['items'][0]['id']
#     categoryId = response['items'][0]['snippet']['categoryId']
#     publishedAt = response['items'][0]['snippet']['publishedAt'] # .split('.')[0] #TODO: Replace "T" by " " so that "2019-05-10T21:49:00" becomes "2019-05-10 21:49:00"
#     description = response['items'][0]['snippet']['description']
#     favoriteCount = response['items'][0]['statistics']['favoriteCount']
#     viewCount = response['items'][0]['statistics']['viewCount']
#     likeCount = response['items'][0]['statistics']['likeCount']
#     dislikeCount = response['items'][0]['statistics']['dislikeCount']

#     # print(response['items'][0])

#     if 'commentCount' in response['items'][0]['statistics'].keys():
#         commentCount = response['items'][0]['statistics']['commentCount']
#     else:
#         commentCount = ""
    
#     if 'tags' in response['items'][0]['snippet'].keys():
#         tags = response['items'][0]['snippet']['tags']
#     else:
#         tags = []
# #     pprint.pprint(response)
#     youtube_dict = {'videoId':videoId,'channelId': channelId,'channelTitle': channelTitle,'tags':tags,'categoryId':categoryId,'title':title,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount, 'publishedAt':publishedAt, 'description':description}

#     return youtube_dict


# # youtube_search("Stephen Colbert")

# # print(youtube_search(id='6VixqvOcK8E'))

test = []
def youtube_search(ids=[]):
    for id in ids:
        # print(id)
        test.append('someproperty of : ' + id)

    youtube_dict = {'test':test}