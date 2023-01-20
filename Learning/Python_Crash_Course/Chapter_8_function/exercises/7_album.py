# 返回字典

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


album_0 = make_album('zhang xueyou', 'kiss goodbye', songs_number=10)
print(album_0)
album_1 = make_album('liu dehua', 'loveless water')
print(album_1)
album_2 = make_album('wang xinlin', 'love you', songs_number=8)
print(album_2)
