from sqlite3 import Date
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Semester(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    weight = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    semester = models.ForeignKey(
        Semester, related_name="projects", on_delete=models.CASCADE, default=1,  db_constraint=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
