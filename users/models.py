from django.db import models
from django.contrib.auth.hashers import make_password
from multiselectfield import MultiSelectField 

# List of possible music talents
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

# List of possible music genres
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

class Artist(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Secure password storage
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Multi-select fields
    talents = MultiSelectField(choices=TALENT_CHOICES, blank=True, null=True)
    genres = MultiSelectField(choices=GENRE_CHOICES, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):  
            self.password = make_password(self.password)  # Hash password before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom} (Artist)"


class Producer(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Secure password storage
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    studio_name = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    # Multi-select field
    genres = MultiSelectField(choices=GENRE_CHOICES, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):  
            self.password = make_password(self.password)  # Hash password before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom} (Producer)"
