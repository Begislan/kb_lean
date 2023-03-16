from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Categories(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)
    image = models.ImageField(upload_to='media/photo/%Y/%m/%d')
    count = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class NameCategories(models.Model):
    id_cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Raz(models.Model):
    categori = models.ForeignKey(NameCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self):
        return self.name


class Glav(models.Model):
    razdel = models.ForeignKey(Raz, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    id_glav = models.ForeignKey(Glav, on_delete=models.CASCADE)
    theme = models.TextField()
    full_text = RichTextField()
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self) -> str:
        return self.theme

class News(models.Model):
    title = models.CharField(max_length=250)
    text = RichTextField()
    img =models.ImageField(upload_to='media/photo/%Y/%m/%d')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class About(models.Model):
    img = models.ImageField(upload_to='media/photo/%Y/%m/%d')
    fio = models.CharField(max_length=255)
    slug = models.SlugField(help_text='Поля автоматический заполняется!')
    special = models.CharField(max_length=255)
    phone = PhoneNumberField(unique=True, verbose_name='Телефон номер')
    rezume = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')

    def __str__(self):
        return self.fio

