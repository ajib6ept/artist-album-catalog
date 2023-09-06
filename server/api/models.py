import datetime

from django.db import models


def current_year():
    return datetime.date.today().year


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artist(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Album(BaseModel):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="album"
    )
    release_year = models.IntegerField(default=current_year)

    def __str__(self):
        return f"{self.artist} - {self.release_year}"


class Track(BaseModel):
    TRACK_NAME_LENGTH = 100

    name = models.CharField(max_length=TRACK_NAME_LENGTH)
    album = models.ManyToManyField(
        Album, through="Song", related_name="tracks"
    )

    def __str__(self):
        return self.name


class Song(BaseModel):
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, related_name="track"
    )
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="album"
    )
    number = models.PositiveSmallIntegerField(
        verbose_name="track number in the album"
    )

    def __str__(self):
        return f"№{self.number} - {self.track} - {self.album}"
