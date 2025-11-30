# models.py
from django.db import models
from multiselectfield import MultiSelectField


class LeadModel(models.Model):
    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    CONSULTATION_CHOICES = [
        ('kitchen', 'Kitchen Remodeling'),
        ('bathroom', 'Bathroom Remodeling'),
        ('garage', 'Garage Remodeling'),
        ('fullhouse', 'Full House Remodeling'),
        ('newconstruction', 'New Construction'),
        ('adu', 'ADU'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    consultation_types = MultiSelectField(choices=CONSULTATION_CHOICES, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead Request #{self.id} from {self.name}"
