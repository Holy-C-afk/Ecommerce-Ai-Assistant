from django.db import models

# Create your models here.

class Analytics(models.Model):
    total_sales = models.PositiveIntegerField(default=0)
    best_seller = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Sales: {self.total_sales}, Best Seller: {self.best_seller}"
