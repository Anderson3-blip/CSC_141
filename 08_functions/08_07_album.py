def make_album(artist, title):
    """build a dictionary containing information about an album"""
    album_dict = {
        'artist' : artist.title(),
        'title' : title.title()
        }
    return album_dict

album = make_album('dax', 'love hurts')
print(album)

album = make_album('True', 'Hulvey')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

# number of songs

def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict


album = make_album('dax', 'love hurts')
print(album)

album = make_album('True', 'Hulvey')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('true','cry', num_songs=10)
print(album)