from django.db import models


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=300)
    ratings = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.id + self.name + self.descriptions + self.ratings
