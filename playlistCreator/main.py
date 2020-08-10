import os

root_android = '/storage/emulated/0/Music/'
root_win = 'C:\\Users\\dreve\\Music\\music'  #
files = []


def make_playlist_name(path):
    folder_name = path.replace(root_win, '')
    return folder_name[1:]


def create_m3u(path, name):
    songs = []
    for entry_name in os.listdir(path):
        entry_dir = path + os.sep + entry_name
        if os.path.isdir(entry_dir):
            create_m3u(entry_dir)
        else:
            songs.append(entry_name)

    playlist_name = make_playlist_name(path)
    playlist = open(path + os.sep + playlist_name, 'w')

    for i in range(len(songs)):
        playlist.write(root_android + path.replace(root_win, '') + songs[i])

    playlist.close()


def mykey(s):
    id = s.split(' ')[0]
    numbers = id.split('.')
    numbers = numbers[:len(numbers) - 1]
    sum = 0.0
    mult = 1.0
    for number in numbers:
        sum += int(number) * mult
        mult /= 1000
    return sum


songs = []
for entry_name in os.listdir(root_win):
    entry_dir = root_win + os.sep + entry_name
    if not os.path.isdir(entry_dir):
        if entry_name.split('.')[0].isdigit():
            songs.append(entry_name)
        else:
            print(entry_name)

# songs = sorted(songs, key=mykey)
songs.sort(key=mykey, reverse=True)

playlist_name = 'Music'
playlist = open('test.txt', 'w+', encoding='utf-8')
playlist.write('#EXTM3U\n')

for i in range(len(songs)):
    playlist.write(root_android + 'music/' + songs[i] + '\n')
    #playlist.write(root_win + '\\' + songs[i] + '\n')

playlist.close()
