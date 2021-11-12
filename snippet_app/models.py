import datetime
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Tag(models.Model):
    title = models.CharField(max_length=128, unique=True)


class Snippet(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            obj, created = Tag.objects.get_or_create(title=self.title)
            self.tag = obj

        return super(Snippet, self).save(*args, kwargs)





