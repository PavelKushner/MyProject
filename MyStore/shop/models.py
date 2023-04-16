from decimal import Decimal

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='продукт',
        unique=True,
        blank=False,
        null=False
    )

    descr = models.CharField(
        max_length=4096,
        verbose_name='описание',
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name='картинка',
        upload_to='product/',
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория',
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='цена',
        null=False,
        blank=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=False,
        blank=False
    )

    disc = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='скидка',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт',
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='категория',
        unique=True,
        null=False,
        blank=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория',
        verbose_name_plural = 'категории'


class Team(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='имя',
        unique=True,
        blank=False,
        null=False
    )

    job_title = models.CharField(
        max_length=64,
        verbose_name='должность',
        blank=False,
        null=False
    )

    image = models.ImageField(
        verbose_name='фото',
        upload_to='team/',
        null=True,
        blank=True
    )

    descr = models.CharField(
        max_length=4096,
        verbose_name='описание',
        default='пусто',
        blank=False,
        null=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=False,
        blank=False
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'команда',
        verbose_name_plural = 'команда'


class AboutUs(models.Model):
    char = models.CharField(
        max_length=32,
        verbose_name='сильные cтороны',
        null=False,
        blank=False
    )

    descr = models.CharField(
        max_length=4096,
        verbose_name='описание',
        default='есть причины',
        null=False,
        blank=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.char

    class Meta:
        verbose_name = 'преимущество',
        verbose_name_plural = 'преимущества'


class Blog(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='блог',
        unique=True,
        blank=False,
        null=False
    )

    body = models.CharField(
        max_length= 3072,
        verbose_name='текст поста',
        blank=False,
        null=False
    )

    image = models.ImageField(
        verbose_name='фото',
        upload_to='blog/',
        null=True,
        blank=True
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блог',
        verbose_name_plural = 'блоги'


class Promotion(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='акция',
        blank=False,
        null=False
    )

    image = models.ImageField(
        verbose_name='банер акции',
        upload_to='promotion/',
        blank=False,
        null=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'акция',
        verbose_name_plural = 'акции'


class Insta(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='низвание',
        blank=False,
        null=False
    )

    image = models.ImageField(
        verbose_name='фото',
        upload_to='insta/',
        blank=False,
        null=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'интсанрам',
        verbose_name_plural = 'инстаграм'


class Gallery(models.Model):
    name = models.CharField(
        max_length=16,
        verbose_name='название',
        null=False,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='категория'
    )

    image = models.ImageField(
        verbose_name='фото',
        upload_to='gallery/',
        blank=False,
        null=False
    )

    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'галерея',
        verbose_name_plural = 'галереи'


class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
   is_paid = models.BooleanField(default=False)

   def __str__(self):
       return f'Order:{self.pk}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Order {self.order} Product {self.product}'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(verbose_name='email', blank=False, null=False)
    subject = models.CharField(max_length=32, verbose_name='тема', blank=False, null=False)
    message = models.CharField(max_length=4000, verbose_name='письмо', blank=False, null=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'сообщение',
        verbose_name_plural = 'сообщения'


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(default='111@gmai.com', verbose_name='email', blank=False, null=False)
    name = models.CharField(max_length=32, verbose_name='имя', blank=False, null=False)
    image = models.ImageField(verbose_name='аватар', upload_to='profile/', null=False, blank=False)
    slug = models.SlugField(verbose_name='URL', unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
