class Song:

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.artist = kwargs['artist']
        self.album = kwargs['album']
        self.length = kwargs['length']

    def __str__(self):
        return '{} - {} from {} - {}'.format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return 'Song(title="' + self.title + '", artist="' + self.artist + '", album="' + self.album + '", length="' + self.get_length() + '")'

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # def __eq__(self, other):
        # isName = self.title == other.title
        # isArtist = self.artist == other.artist
        # isAlbum = self.album == other.album
        # isLength = self.length == other.length
        # return isName and isArtist and isAlbum and isLength

    def get_length(self, **kwargs):
        length = self.length
        seconds = makeToSeconds(length)
        if 'seconds' in kwargs and kwargs['seconds'] == True:
            return seconds
        elif 'minutes' in kwargs and kwargs['minutes'] == True:
            return seconds // 60
        elif 'hours' in kwargs and kwargs['hours'] == True:
            return seconds // 3600
        else:
            return length

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}

def makeToSeconds(length_str):
    length = int(length_str[-2:])
    while(len(length_str) > 2):
        if ':' in length_str:
            length_str = length_str[:-3]
            length += int(length_str[-2:]) * 60
    return length
