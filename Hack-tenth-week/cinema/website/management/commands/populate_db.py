from django.core.management.base import BaseCommand
from website.models import Movie, Projection, Reservation


class Command(BaseCommand):

    def _add_movies(self):
        Movie.add_movie(name='The Green Mile', rating=9.0)
        Movie.add_movie(name='Stay Alive', rating=6.0)
        Movie.add_movie(name='Twenty-Seven Dresses', rating=5.0)
        Movie.add_movie(name='Inception', rating=9.0)
        Movie.add_movie(name='The Hunger Games: Catching Fire', rating=7.9)
        Movie.add_movie(name='Wreck-It Ralph', rating=7.8)
        Movie.add_movie(name='Her', rating=8.3)

    def _delete_movies(self):
        Movie.objects.all().delete()

    def _delete_projections(self):
        Projection.objects.all().delete()

    def _add_projections(self):
        Projection.add_projection(movie=Movie.objects.get(name='The Green Mile'), type_projection='3D', date='2015-05-19', time='18:00')
        Projection.add_projection(movie=Movie.objects.get(name='Stay Alive'), type_projection='3D', date='2015-05-19', time='18:00')
        Projection.add_projection(movie=Movie.objects.get(name='Twenty-Seven Dresses'), type_projection='3D', date='2015-05-19', time='18:00')
        Projection.add_projection(movie=Movie.objects.get(name='Inception'), type_projection='3D', date='2015-05-19', time='18:00')
        Projection.add_projection(movie=Movie.objects.get(name='The Hunger Games: Catching Fire'), type_projection='3D', date='2015-05-19', time='18:00')
        Projection.add_projection(movie=Movie.objects.get(name='Wreck-It Ralph'), type_projection='3D', date='2015-05-19', time='18:00')

    def _add_reservations(self):
        Reservation.add_reservation(username='desi', row='1', col='1', projection=Projection.objects.get(movie__name='The Green Mile'))
        Reservation.add_reservation(username='marmot', row='1', col='1', projection=Projection.objects.get(movie__name='Inception'))

    def handle(self, *args, **options):
        self._add_movies()
        self._add_projections()
        self._add_reservations()
