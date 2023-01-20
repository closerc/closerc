# while 与函数结合

def make_album(singer_name, album_name, songs_number=''):
    """返回包含有关一张专辑的信息

    Args:
        singer_name (str): 歌手名
        album_name (str): 专辑名
        songs_number (str, optional): 歌曲数. Defaults to ''.
    """
    album = {'singer_name': singer_name, 'album_name': album_name}
    if songs_number:
        album['songs_number'] = songs_number
    return album


while True:
    print("\nPlease tell me a album's singer and name:")
    print("(enter 'q' at any time to quit)")
    singer = input("Singer name: ")
    if singer == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break
    user_album = make_album(singer, album_name)
    print(user_album)
