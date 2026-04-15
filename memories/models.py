from django.db import models


class Memory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название места")
    description = models.TextField(blank=True, verbose_name="Описание")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    image = models.ImageField(upload_to='memories/', blank=True, null=True, verbose_name="Фото")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
