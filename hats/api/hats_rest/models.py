from django.db import models
from django.urls import reverse

class LocationVO(models.Model):
    import_href = models.URLField(max_length=200, unique=True)
    closet_name = models.CharField(max_length=200)

class Hats(models.Model):
    fabric = models.CharField(max_length=200)
    style_name = models.CharField(max_length = 200)
    color = models.CharField(max_length = 200)
    picture_url = models.URLField()
    location = models.ForeignKey(
        LocationVO,
        related_name="hat",
        on_delete=models.CASCADE,
        null=True,
    )
    def get_api_url(self):
        return reverse("api_show_hat", kwargs={"id": self.id})

    def __str__(self):
        return self.style_name

    class Meta:
        ordering = ("style_name",)
