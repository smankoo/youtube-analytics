from pytube import Playlist
import re
import json
import os

with open ('settings.json', 'rb') as jsonfile:
    settings = json.load(jsonfile)

WORKING_DIR = settings['WORKING_DIR']

if not os.path.exists(WORKING_DIR):
    os.makedirs(WORKING_DIR)

# pl = Playlist('https://www.youtube.com/channel/UCMtFAi84ehTSYSE9XoHefig/videos')

# Late show with Stephen Colbert - https://www.youtube.com/channel/UCMtFAi84ehTSYSE9XoHefig/videos

# pl = Playlist('https://www.youtube.com/channel/UCMtFAi84ehTSYSE9XoHefig/videos')

# pl = Playlist('https://www.youtube.com/watch?v=OuNfGc7sM2Y&list=PLpHbno9djTOR4-E0E4O7SbSLgnoRw929p')

# AIB Channel
pl = Playlist('https://www.youtube.com/user/allindiabakchod/videos')

pl.populate_video_urls()

videoIds = []

for url in pl.video_urls:
    for argval in url.split('?')[1].split('&'):
        arg=argval.split('=')[0]
        val=argval.split('=')[1]
        if arg == 'v':
            videoId = val
            videoIds.append(videoId)

video_ids_dict = {'videoIds': videoIds}
print(video_ids_dict)

with open(WORKING_DIR + '/' + 'video_ids.json', 'w') as jsonfile:
    json.dump(video_ids_dict, jsonfile)

jsonfile.close()
