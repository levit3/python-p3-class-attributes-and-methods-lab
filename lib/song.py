class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__ (self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, self):
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)
            
    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)
            
    @classmethod
    def add_to_genre_count(cls, self):
        cls.genre_count[self.genre] = self.genre_count.get(self.genre, 0) + 1
    
    @classmethod
    def add_to_artist_count(cls, self):
        cls.artist_count[self.artist] = cls.artist_count.get(self.artist, 0) + 1
