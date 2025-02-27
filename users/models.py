from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)


# Liste des talents musicaux possibles
TALENT_CHOICES = [
    ('singer', 'Chanteur/Chanteuse'),
    ('rapper', 'Rappeur/Rappeuse'),
    ('guitarist', 'Guitariste'),
    ('pianist', 'Pianiste'),
    ('drummer', 'Batteur/Batteuse'),
    ('violinist', 'Violoniste'),
    ('bassist', 'Bassiste'),
    ('composer', 'Compositeur/Compositrice'),
    ('dj', 'DJ'),
    ('lyricist', 'Parolier/Parolière'),
]

# Liste des genres musicaux possibles
GENRE_CHOICES = [
    ('pop', 'Pop'),
    ('rock', 'Rock'),
    ('hiphop', 'Hip-Hop'),
    ('rap', 'Rap'),
    ('jazz', 'Jazz'),
    ('classical', 'Classique'),
    ('electronic', 'Électronique'),
    ('rnb', 'R&B'),
    ('reggae', 'Reggae'),
    ('blues', 'Blues'),
    ('metal', 'Metal'),
    ('country', 'Country'),
    ('soul', 'Soul'),
]

# Modèle pour les artistes
class Artist(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    talents = models.JSONField(default=list, blank=True, null=True)  # Liste de talents
    genres = models.JSONField(default=list, blank=True, null=True)  # Liste de genres
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} (Artist)"

# Modèle pour les producteurs
class Producer(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    studio_name = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    genres = models.JSONField(default=list, blank=True, null=True)  # Liste de genres
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} (Producer)"
