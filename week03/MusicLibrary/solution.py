from music_library import Song, PlayList

def main():
    song1 = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
    song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
    song3 = Song(title="7 Rings", artist="Ariana Grande", album="Thank U, Next", length="4:44")
    song4 = Song(title="Tank U, Next", artist="Ariana Grande", album="Thank U, Next", length="4:44")

    playlist = PlayList(name = "My New PlayList", repeat = True, shuffle = True)
    playlist.add_songs([song1, song2, song3, song4])

    playlist.save()
    playlist2 = PlayList.load("My-New-PlayList.json")
    print(playlist2.name == "My New PlayList")


if __name__ == '__main__':
 	main()
