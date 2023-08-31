from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=False)
    description = models.CharField(max_length=2000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to="ads/media", null=True, blank=True)

    def __str__(self):
        return self.title

    def is_valid(self):
        pass

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'
        ordering = ['created_at']


class Comment(models.Model):
    text = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def is_valid(self):
        pass
