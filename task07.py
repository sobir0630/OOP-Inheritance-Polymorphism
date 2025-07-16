class Media:
    def __init__(self, title):
        self.title = title

    def play(self):
        return "Media fayl ijro etilmoqda."

class Song(Media):
    def play(self):
        return f"Qoshiq ijro etilmoqda: '{self.title}'"

class Movie(Media):
    def play(self):
        return f"Film namoyish etilmoqda: '{self.title}'"

class Podcast(Media):
    def play(self):
        return f"Podkast eshittirilmoqda: '{self.title}'"

song = Song("Orzular")
movie = Movie("Yulduzlar orasida")
podcast = Podcast("Dasturchilar hayoti")

print(song.play())
print(movie.play())
print(podcast.play())
