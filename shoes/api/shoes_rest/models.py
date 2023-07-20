from django.db import models
from django.urls import reverse

# Create your models here.


class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField(null=True)
    bin_size = models.PositiveSmallIntegerField(null=True)
    import_href = models.URLField(max_length=200, null=True, unique=True)


class Shoe(models.Model):
    Manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.URLField(null=True, blank=True)
    bin = models.ForeignKey(
        BinVO,
        related_name='shoes',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.model_name

    def get_api_url(self):
        return reverse("api_show_shoes", kwargs={"pk": self.pk})
