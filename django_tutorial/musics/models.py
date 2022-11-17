from django.db import models

# Create your models here.
GENRE_CHOICES = (
    ('RK', 'ROCK'),
    ('JZ', 'JAZZ'),
    ('CS', 'CLASSIC'),
    ('JP', 'J-POP'),
)
class Music(models.Model):
    song = models.TextField(default="song") #input text
    singer = models.TextField(default="Rain Turn Soup")
    last_modfify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    genre = models.CharField(       #checklist
        max_length = 2,
        choices = GENRE_CHOICES,
        default = "RK"
    )    
    class Meta:
        db_table = "music"
    
    def display_type_name(self):
        return self.get_genre_display()
