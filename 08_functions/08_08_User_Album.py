def make_album(artist, title, tracks=0):
    """build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    
    if tracks:
        album_dict['tracks'] = tracks
        return album_dict
    

# prepare promps

title_prompt = "\nWhat album are you thinking of?"
artist_prompt = "who is the artist?"

# user quit
print("enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("Thank you for responding!")