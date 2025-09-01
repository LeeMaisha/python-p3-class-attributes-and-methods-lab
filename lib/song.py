class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every time we create a new song, update counters and lists
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        """Add unique artists only"""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        """Add unique genres only"""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment histogram for artist count"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment histogram for genre count"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
god_plan = Song("God's Plan", "Drake", "Rap")

print(Song.count)  
# 3

print(Song.artists)  
# ['Jay-Z', 'Beyonce', 'Drake']

print(Song.genres)  
# ['Rap', 'Pop']

print(Song.genre_count)  
# {'Rap': 2, 'Pop': 1}

print(Song.artist_count)  
# {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}