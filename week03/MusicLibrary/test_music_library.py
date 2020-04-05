import unittest
from music_library import Song, PlayList


class TestSong(unittest.TestCase):
    def test_printing_the_song(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

        self.assertEqual(str(song), "Manowar - Odin from The Sons of Odin - 3:44")

    def test_if_two_song_are_equal_after_equalization(self):
        song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

        self.assertEqual(song1, song2)

    def test_if_argument_seconds_is_true_returns_length_in_seconds_and_the_length_has_no_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

        res = song.song_length(seconds=True)

        self.assertEqual(res, 224)

    def test_if_argument_seconds_is_true_returns_length_in_seconds_and_the_length_has_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")

        res = song.song_length(seconds=True)

        self.assertEqual(res, 5444)

    def test_if_argument_minutes_is_true_returns_length_in_minutes_and_the_length_has_no_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

        res = song.song_length(minutes=True)

        self.assertEqual(res, 3)

    def test_if_argument_minutes_is_true_returns_length_in_minutes_and_the_length_has_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")

        res = song.song_length(minutes=True)

        self.assertEqual(res, 90)

    def test_if_argument_hours_is_true_returns_the_length_in_hours_and_the_length_has_no_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="30:44")

        res = song.song_length(hours=True)

        self.assertEqual(res, 0)

    def test_if_argument_hours_is_true_returns_the_length_in_hours_and_the_length_has_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")

        res = song.song_length(hours=True)

        self.assertEqual(res, 1)

    def test_if_there_are_no_arguments_returns_the_string_representation_of_the_length(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:30:44")

        res = song.song_length()

        self.assertEqual(res, "1:30:44")


class TestPlayList(unittest.TestCase):

    def test_adding_songs_to_the_play_list_return_a_string_representationof_the_total_length_of_all_songs_with_no_hours(self):
        song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(title="7 Rings", artist="Ariana Grande", album="Thank U, Next", length="4:44")

        play_list = PlayList(name="My New PlayList")

        play_list.add_song(song1)
        play_list.add_song(song2)

        res = play_list.total_length()

        self.assertEqual(res, "0:08:28")

    def test_adding_songs_to_the_play_list_return_a_string_representationof_the_total_length_of_all_songs_with_hours(self):
        song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:13:04")
        song2 = Song(title="7 Rings", artist="Ariana Grande", album="Thank U, Next", length="4:44")

        play_list = PlayList(nam="My New PlayList", repeat=True, shuffle=True)

        play_list.add_song(song1)
        play_list.add_song(song2)

        res = play_list.total_length()

        self.assertEqual(res, "1:17:48")

    def test_adding_ongs_to_the_playlist_return_a_divtionary_with_artists_and_count_of_songs_they_have_in_the_playlist(self):
        song1 = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
        song3 = Song(title="7 Rings", artist="Ariana Grande", album="Thank U, Next", length="4:44")
        song4 = Song(title="Tank U, Next", artist="Ariana Grande", album="Thank U, Next", length="4:44")

        play_list = PlayList(name="My New PlayList", repeat=True, shuffle=True)

        play_list.add_song(song1)
        play_list.add_song(song2)
        play_list.add_song(song3)
        play_list.add_song(song4)

        dic = play_list.artists()

        self.assertEqual(dic, {'Manowar1': 1, 'Manowar2': 1, 'Ariana Grande': 2})


if __name__ == '__main__':
    unittest.main()
