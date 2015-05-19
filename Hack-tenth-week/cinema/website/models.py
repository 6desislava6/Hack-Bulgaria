from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    cover = models.ImageField()

    @classmethod
    def add_movie(cls, **kwargs):
        movie = cls(name=kwargs['name'], rating=kwargs['rating'])
        movie.save()

    def __str__(self):
        return '{} - {}'.format(self.name, self.rating)

    def __hash__(self):
        return hash(self.name)


# 1 movie - MANY projections 1:N
class Projection(models.Model):
    movie = models.ForeignKey(Movie)
    type_projection = models.CharField(max_length=6)
    date = models.DateField()
    time_projection = models.TimeField()

    @classmethod
    def add_projection(cls, **kwargs):
        projection = cls(movie=kwargs['movie'], type_projection=kwargs[
                         'type_projection'], date=kwargs[
                         'date'], time_projection=kwargs[
                         'time'])
        projection.save()

    @classmethod
    def show_movie_projections(cls, movie_id):
        projections = Projection.objects.filter(movie__id=movie_id)
        return projections

    def __str__(self):
        return """{} - {} - {} - {}""".format(self.movie.name, self.type_projection, self.date, self.time_projection)

class Reservation(models.Model):
    username = models.CharField(unique=True, max_length=20)
    projection = models.ForeignKey(Projection)
    row = models.IntegerField()
    col = models.IntegerField()

    @classmethod
    def add_reservation(cls, **kwargs):
        reservation = cls(username=kwargs['username'], projection=kwargs[
                         'projection'], row=kwargs[
                         'row'], col=kwargs[
                         'col'])
        reservation.save()

    def __str__(self):
        return """username: {},
projection: {},
row: {}, col: {} """.format(self.username, self.projection, self.row, self.col)
