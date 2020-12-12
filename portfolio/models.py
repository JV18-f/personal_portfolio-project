from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)  # blank=True means filling url isn't required

    def __str__(self):  # what is the default name of the Project
        return self.title
