from django.db import models


class Location(models.Model):
    date = models.DateField()
    lat = models.DecimalField(max_digits=6, decimal_places=4)
    lon = models.DecimalField(max_digits=7, decimal_places=4)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    @property
    def temperatures(self):
        return Temperatures.objects.filter(location=self).values_list('temperatures', flat=True)


class Temperatures(models.Model):
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    temperatures = models.DecimalField(max_digits=3, decimal_places=1)


