import random


# ========= Your classes ==========
class Settings:

    def __init__(self, shuffle, repeat):
        self.shuffle = shuffle
        self.repeat = repeat


class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __eq__(self, other):
        return isinstance(other, Song) \
               and self.title == other.title \
               and self.artist == other.artist \
               and self.duration == other.duration

    def __str__(self):
        return "{} - {}: {}".format(self.title, self.artist, self.duration)


class Playlist:

    def __init__(self, title, songs):
        self.__title = title
        self.__songs = songs
        self.__current_song = None
        self.__last_song = songs[len(songs) - 1]

    def get_title(self):
        return self.__title

    def get_song_titles(self):
        songs_list = []
        for song in self.__songs:
            songs_list.append(song.title)

        return songs_list

    def load_song_by_title(self, title):

        for song in self.__songs:
            if song.title == title:
                self.__current_song = song
                return song

    def load_next_song(self, shuffle, repeat):

        if shuffle:
            self.__current_song = random.choice(self.__songs)
            return self.__current_song

        elif repeat:
            if self.__current_song == self.__last_song:
                self.__current_song == self.__songs[0]
                return self.__current_song
            else:
                current_index = self.__songs.index(self.__current_song)
                self.__current_song = self.__songs[current_index + 1]
                return self.__current_song

        elif not shuffle and not repeat:
            if self.__current_song == self.__last_song:
                self.__current_song = None
                return None
            else:
                if self.__current_song is None:
                    self.__current_song = self.__songs[0]
                    return self.__current_song
                else:
                    current_index = self.__songs.index(self.__current_song)
                    self.__current_song = self.__songs[current_index + 1]
                    return self.__current_song

    def get_last_song(self):
        return self.__last_song


class Spotify:

    def __init__(self, playlist, settings):
        self.__playlist = playlist
        self.__settings = settings
        self.__current_song = None
        self.__is_playing = False

    def get_current_song(self):
        return self.__current_song

    def is_playing(self):
        if self.__is_playing:
            return True

        else:
            return False

    def get_playlist_title(self):
        return self.__playlist.get_title()

    def play(self, title=""):
        if title != "":
            self.__current_song = self.__playlist.load_song_by_title(title)
            self.__is_playing = True

        elif self.__current_song is None:
            self.__current_song = self.__playlist.load_next_song(self.__settings.shuffle, self.__settings.repeat)
            self.__is_playing = True

        elif self.__current_song is not None and not self.__is_playing:
            self.__is_playing = True

        elif self.__is_playing:
            pass

    def pause(self):
        self.__is_playing = False

    def next(self):
        if self.__current_song == self.__playlist.get_last_song():
            self.__playlist.load_next_song(False, False)
            self.__current_song = None
            self.__is_playing = None
            return None
        next_song = self.__playlist.load_next_song(self.__settings.shuffle, self.__settings.repeat)
        self.__current_song = next_song

        if self.__current_song is None:
            self.__is_playing = False
        else:
            self.__is_playing = True


# =================================

if __name__ == '__main__':
    no_repeat_no_shuffle = Settings(False, False)

    songs = [Song("Hotel California", "Eagles", 390),
             Song("Harder Better Faster Stronger", "Daft Punk", 224),
             Song("2112", "Rush", 1233)]
    playlist = Playlist("MyPlaylist", songs)

    player = Spotify(playlist, no_repeat_no_shuffle)

    assert player.get_playlist_title() == "MyPlaylist"

    assert playlist.get_song_titles() == ["Hotel California", "Harder Better Faster Stronger", "2112"]

    assert playlist.load_next_song(False, False) == Song("Hotel California", "Eagles", 390)
    assert playlist.load_next_song(False, False) == Song("Harder Better Faster Stronger", "Daft Punk", 224)
    assert playlist.load_next_song(False, False) == Song("2112", "Rush", 1233)
    assert not playlist.load_next_song(False, False)

    assert playlist.load_song_by_title("2112") == Song("2112", "Rush", 1233)

    # Reset playlist
    playlist = Playlist("MyPlaylist", songs)

    player = Spotify(playlist, no_repeat_no_shuffle)

    # Should be first song, playing
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    # Should not change song or playing
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    # Should not change song, playing is False
    player.pause()
    assert player.get_current_song() == songs[0]
    assert not player.is_playing()

    # Should not change song, playing back to True
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    # Should change song, playing True
    player.next()
    assert player.get_current_song() == songs[1]
    assert player.is_playing()

    # Should change song, playing True
    player.next()
    assert player.get_current_song() == songs[2]
    assert player.is_playing()

    # No songs left, song == None and playing False
    player.next()
    assert not player.get_current_song()
    assert not player.is_playing()

    # Load song by title
    player.play("2112")
    assert player.get_current_song() == songs[2]
    assert player.is_playing()

    # Previous song was last in playlist, next should return None, playing False
    player.next()
    assert not player.get_current_song()
    assert not player.is_playing()

    # Start playlist
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    player.next()
    player.next()
    player.next()
    assert not player.get_current_song()
    assert not player.is_playing()

    # When playlist is finished, calling next starts playlist again.
    player.next()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()
