from django.db import models
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Titulo")
    text = models.TextField(verbose_name="Sinopsis")
    categories = models.ManyToManyField(Category, verbose_name="Categorías")
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'images')
    contentvid = models.FileField(verbose_name = 'Video', upload_to='videos')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Creacion de publicaión')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Actualización de publicaión')

    class Meta:
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicaciones'
        ordering = ['-created'] 

    def __str__(self):
        return self.title