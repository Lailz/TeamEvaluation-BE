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


class Criteria(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    weight = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    criterias = models.ManyToManyField(Criteria)
    semester = models.ForeignKey(
        Semester, related_name="projects", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Team(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(
        Project, related_name="teams", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Report(models.Model):
    grade = models.IntegerField()
    judge = models.CharField(max_length=50, default="Lailz")
    team = models.ForeignKey(
        Team, related_name="grades", on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, related_name="grades", on_delete=models.CASCADE)

    def __str__(self):
        return f"Team: {self.team}, Project: {self.project} - Judged by: {self.judge}"
