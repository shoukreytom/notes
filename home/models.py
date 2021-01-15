from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from account.models import Account


class Note(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Note)
def save_slug(sender, created, instance, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title + str(instance.updated))
        instance.save()
