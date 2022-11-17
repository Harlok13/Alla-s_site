from django.db import models
from django.urls import reverse


class Posts(models.Model):
    """Посты"""
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='archive/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create', 'title']


    class Category(models.Model):
        """Категории"""
        name = models.CharField(max_length=200, verbose_name='Название')
        slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse('category', kwargs={'category_slug': self.slug})

        class Meta:
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'







