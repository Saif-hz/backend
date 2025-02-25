from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


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

class User(AbstractUser):
    ROLE_CHOICES = [
        ('artist', 'Artist'),
        ('producer', 'Producer'),
    ]

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_de_naissance = models.DateField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nom', 'prenom', 'date_de_naissance', 'role']

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.role})"


class Artist(User):
    talents = models.ManyToManyField("Talent", related_name="artists", blank=True)
    genres = models.ManyToManyField("Genre", related_name="artists", blank=True)


class Producer(User):
    studio_name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    genres = models.ManyToManyField("Genre", related_name="producers", blank=True)


class Talent(models.Model):
    name = models.CharField(max_length=50, choices=TALENT_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()


class Genre(models.Model):
    name = models.CharField(max_length=50, choices=GENRE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()
