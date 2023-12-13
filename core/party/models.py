import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=200)
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organized_parties",
    )

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return f"{self.venue}, {self.party_date}"


class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gift = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.gift


class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="guests")

    def __str__(self):
        return str(self.name)
