from django.db import models

# Create your models here.

class DescriptionRequest(models.Model):
    keywords = models.CharField(max_length=255)
    generated_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keywords
