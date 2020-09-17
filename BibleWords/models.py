from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=250, unique=True)
    audio_src = models.CharField(max_length=250,unique=True)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.word
    
    