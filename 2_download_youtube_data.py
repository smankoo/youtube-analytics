import json
import csv
import os
from youtube_data import youtube_search_batch

WORKING_DIR = 'tmp'
OUT_FILE = WORKING_DIR + '/' +'youtube_data.csv'

with open (WORKING_DIR + '/' +'video_ids.json', 'rb') as jsonfile:
    video_ids_json = json.load(jsonfile)

total_videos = len(video_ids_json['videoIds'])
print("Total videos: " + str(total_videos))
print("Starting data collection...")
i = 0
youtube_data = []

test_data = video_ids_json['videoIds']
youtube_data = youtube_search_batch(ids=test_data)


if os.path.exists(OUT_FILE):
    open_mode = 'a'
else:
    open_mode = 'w'

with open(OUT_FILE, open_mode, encoding='utf-8') as f:
    keys = youtube_data[0].keys()
    w = csv.DictWriter(f, quoting=csv.QUOTE_ALL, lineterminator='\n', fieldnames=keys)
    if(open_mode == 'w'):
        w.writeheader()
    for row in youtube_data:
        w.writerow(row)

print("Completed data collection.")

