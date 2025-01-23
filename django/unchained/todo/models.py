from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Manga information generelt her vi har manager stored
class Manga(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to="covers/") # imagefield = billede
    description = models.TextField(max_length=100)
    genre = models.CharField(max_length=100)
    written = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

cote = Manga("Classroom Of The Elite",)


# Favorite feature where users can mark a manga as a favorite
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites") # dette er at mangaen er knyttet til en bruger, hvis brugeren slettes så er manager favorit væk også.
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name="favorites")
    favorited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.manga.title}"