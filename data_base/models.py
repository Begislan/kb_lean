from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Categories(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="категория")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)
    image = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение категории")
    count = models.IntegerField(verbose_name="номер категории")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class NameCategories(models.Model):
    id_cat = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Из какого категории")
    title = models.CharField(max_length=100, verbose_name="название предмета")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Предмет '
        verbose_name_plural = 'Предметы категории'


class Raz(models.Model):
    categori = models.ForeignKey(NameCategories, on_delete=models.CASCADE, verbose_name="Из какого предмета")
    name = models.CharField(max_length=250, verbose_name="раздел предмета")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Раздел предмета'


class Glav(models.Model):
    razdel = models.ForeignKey(Raz, on_delete=models.CASCADE, verbose_name="Из какого раздела")
    name = models.CharField(max_length=250, verbose_name="глава раздела")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Глава раздела'


class Theme(models.Model):
    id_glav = models.ForeignKey(Glav, on_delete=models.CASCADE, verbose_name="Из какого глава")
    theme = models.TextField(verbose_name="Тема:")
    full_text = RichTextField(verbose_name="Тексе:")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self) -> str:
        return self.theme

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Тема главы'


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название новости")
    text = RichTextField(verbose_name="Текст:")
    img = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение новость", blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="дата новость 'автоматически заполняется'")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class About(models.Model):
    img = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение работника")
    fio = models.CharField(max_length=255, verbose_name="Фамилия, Имя, Отечества")
    slug = models.SlugField(help_text='Поля автоматический заполняется!')
    special = models.CharField(max_length=255, verbose_name="специалисть")
    phone = PhoneNumberField(unique=True, verbose_name='Телефон номер', blank=True)
    rezume = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d', verbose_name="резюме необезательно")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
