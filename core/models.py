from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre', unique=True)
    active = models.BooleanField(default=True, verbose_name='activo')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre', unique=True)
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='Bajada')
    # ckeditor
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='post', verbose_name='Imagen', null=True, blank=True)
    published = models.BooleanField(default=False, verbose_name='Publicado')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de actualizacion')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoria')
    tag = models.ManyToManyField(Tag, verbose_name='Etiqueta')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    description = models.CharField(max_length=250, verbose_name='Descripcion')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de nosotros'
        ordering = ['description',]
    
    def __str__(self):
        return self.description
    
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='key Link')
    name = models.CharField(max_length=100, verbose_name='Red Social')
    url = models.URLField(max_length=350, blank=True, null=True, verbose_name='Enlace')
    icon = models.CharField(max_length=100, verbose_name='Icono')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['name',]
    def __str__(self):
        return self.name