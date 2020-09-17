from django.db import models
from django.conf import settings
from audiofield.fields import AudioField
import os.path


class Song(models.Model):
    Artist = models.CharField(max_length=250)
    SongTitle = models.CharField(max_length=250)
    # Add the audio field to your model
    audio = AudioField(upload_to='media/upload/', blank=True,
                            ext_whitelist=(".mp3", ".wav", ".ogg"),
                            help_text=("Allowed type - .mp3, .wav, .ogg"))
    date_added  = models.DateField(auto_now_add=True)
        
        # Add this method to your model
    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
            return player_string

    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')
    def __str__(self):
        return self.Artist + "sang" + SongTitle