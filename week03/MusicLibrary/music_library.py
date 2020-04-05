import datetime
import json


class Song:

    def __init__(self, *, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __repr__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length

    def __hash__(self):
        return hash(self.title, self.artist, self.album, self.length)

    def song_length(self, seconds=False, minutes=False, hours=False):
        new_length = self.length.split(":")

        if seconds:
            if len(new_length) == 3:
                return sum(x * int(t) for x, t in zip([3600, 60, 1], new_length))
            else:
                return sum(x * int(t) for x, t in zip([60, 1], new_length))

        elif minutes:
            if len(new_length) == 3:
                new_length.pop()
                return sum(x * int(t) for x, t in zip([60, 1], new_length))
            else:
                new_length.pop()
                return sum(x * int(t) for x, t in zip([1], new_length))

        elif hours:
            if len(new_length) == 3:
                return int(new_length[0])
            else:
                return 0
        else:
            return self.length


class PlayList:
    def __init__(self, *, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list_with_songs = []

    def add_song(self, song):
        return self.list_with_songs.append(song)

    def remove_song(self, song):
        return self.list_with_songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.list_with_songs.append(song)
        return self.list_with_songs

    def total_length(self):
        lengths_of_songs = []
        for song in self.list_with_songs:
            lengths_of_songs.append(song.song_length())

        sum = datetime.timedelta()
        for i in range(len(lengths_of_songs)):
            song_i_length = lengths_of_songs[i].split(":")

            if len(song_i_length) == 2:
                (m, s) = song_i_length
                d = datetime.timedelta(minutes=int(m), seconds=int(s))
                sum += d
            else:
                (h, m, s) = song_i_length
                d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                sum += d

        return str(sum)

    def artists(self):
        dic = {}
        for song in self.list_with_songs:
            if song.artist in dic:
                dic[song.artist] += 1
            else:
                dic[song.artist] = 1

        return dic

    def save(self):
        dic = {}
        count_of_songs = 0
        for i in range(len(self.list_with_songs)):
            count_of_songs += 1
            dic[str(count_of_songs)] = str(self.list_with_songs[i].__dict__)

        with open(f'playlist-data/{self.name.replace(" ", "-")}.json', 'w') as f:
            json.dump({str(self.name): dic}, f, indent=1)

    @classmethod
    def load(cls, playlist_name):
        new_playlist_name = (playlist_name.replace("-", " ")).replace(".json", "")
        new_list_with_songs = []

        with open(f'playlist-data/{playlist_name}', 'r') as f:
            my_read_object = json.load(f)
            dict_with_all_songs = my_read_object[new_playlist_name]
            for i in range(len(dict_with_all_songs)):
                new_list_with_songs.append(dict_with_all_songs[str(i + 1)])

            new_playlist = cls(name=new_playlist_name, repeat=True, shuffle=True)
            new_playlist.list_with_songs = new_list_with_songs

            return new_playlist
