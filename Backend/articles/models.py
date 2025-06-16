from django.db import models
from .utils import Translator

class Article(models.Model):
    title_en = models.CharField(max_length=255)
    content_en = models.TextField()
    title_so = models.CharField(max_length=255, blank=True)
    content_so = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.title_so or not self.content_so:
            translator = Translator()
            self.title_so = translator.translate_to_somali(self.title_en)
            self.content_so = translator.translate_to_somali(self.content_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en