from django.db import models


class MenuItem(models.Model):
    title = models.CharField(
        max_length=100,
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.title.replace(" ", "-")}'