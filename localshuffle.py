import os
import pprint
import sys
import subprocess
import numpy as np

#  Movie Location
videoextensions = ['mp4', 'm4a', 'm4v', 'f4v', 'f4a',
                   'm4b', 'm4r', 'f4b', 'mov', 'webm', 'wmv',
                   'mkv', 'flv', 'avi']
Episodes = []
player_path = r"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"
watchdir = r"E:\\Stuff\\Netflix"

if sys.platform == 'linux':
    connector = '/'
elif sys.platform == 'win32':
    connector = r'\\'
    

movieorseries = str(input('Do you want to watch a movie or series? '))
categories = str(input('If you further categories your watchables'
                       ' enter your prefered category today: '))
# add either movieorseries or categories to choose between them or both

watchdir = watchdir + connector + movieorseries + connector + categories

items = []
# try:
for foldername, subfolders, filenames in os.walk(watchdir):
    for filename in filenames:
        for extension in videoextensions:
            if filename.endswith(extension):
                folderlist = foldername.split(connector)
                watchlist = watchdir.split(connector)
                show = list(set(watchlist)
                            .symmetric_difference(set(folderlist)))
                if show in items:
                    continue
                else:
                    items.append(show)
# items is a list of list that contains the titles we need
titles = []
for name in items:
    for title in name:
        if len(title) > 10:
            split_titles = title.split('\\')
            for split_title in split_titles:
                titles.append(split_title)

show = set(titles)
things = ['Season {}'.format(x) for x in range(1, 51)]
things.extend(['Season 0{}'.format(x) for x in range(1, 10)])
things.extend(['season {}'.format(x) for x in range(1, 51)])
things.extend(['season 0{}'.format(x) for x in range(1, 10)])
things.extend(['s 0{}'.format(x) for x in range(1, 10)])
things.extend(['s {}'.format(x) for x in range(1, 51)])
things.extend(['Extras', 'extras', 'Shorts', 'shorts', 'Specials', 'specials'])
things.append(categories)

for item in things:
    if item in show:
        show.remove(item)
pprint.pprint(show)

s = 0
while s <= 3:
    favoured = str(input(("Here are the shows present Please"
                          " pick the name of the show you want to watch : ")))
    if favoured in show:
        watchdir2 = watchdir + connector + favoured
        break
    else:
        print("Please enter the correct show you have three more tries")
    s = s + 1

for dirpath, subdirs, files in os.walk(watchdir2):
    for file in files:
        for ending in videoextensions:
            if file.endswith(ending):
                Episodes.append(os.path.join(dirpath, file))

No_episodes = len(Episodes)
print(No_episodes)
random_index = np.random.randint(0, No_episodes)
episode_path = str(Episodes[random_index])
print(episode_path)
subprocess.Popen([player_path, episode_path])

# except:
#     print("The movie or series and or the category you selected don't exist")
# print(Episodes)
