from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def validate_quantity(value):
    if value < 0 or value > 100:
        raise models.ValidationError('Quantity must be between 0 and 100 (inclusive).')
