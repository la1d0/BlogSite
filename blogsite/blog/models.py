from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Article.Status.PUBLISHED)


class Article(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликова'


    title = models.CharField(max_length=255,
                             verbose_name='Заголовок',
                             )
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name='Slug',
                            )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              default=None,
                              blank=True,
                              null=True,
                              verbose_name='Фото',
                              )
    content = models.TextField(blank=True,
                               verbose_name='Текст статьи',
                               )
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Время создания',
                                       )
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name='Время изменения',
                                       )
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT,
                                       verbose_name='Статус',
                                       )
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            related_name='posts',
                            verbose_name='Категории',
                            )
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.SET_NULL,
                               related_name='posts',
                               null=True,
                               default=None,
                               verbose_name='Автор',
                               )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    name = models.CharField(max_length=100,
                            db_index=True,
                            verbose_name='Категория',
                            )
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})