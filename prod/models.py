from django.db import models
from users.models import CustomUser
from django.utils.text import slugify


# Create your models here.
class Sex(models.Model):
    name = models.CharField("Пол", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class WatchType(models.Model):
    name = models.CharField("Тип часов", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип часов'
        verbose_name_plural = 'Типы часов'


class Brand(models.Model):
    name = models.CharField("Бренд часов", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Equipment(models.Model):
    name = models.CharField("Комплектация", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектация'


class MehType(models.Model):
    name = models.CharField("Тип механизма", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип механизма'
        verbose_name_plural = 'Тип механизма'


class Condition(models.Model):
    name = models.CharField("Состояние часов", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состояние часов'
        verbose_name_plural = 'Состояние часов'


class Colour(models.Model):
    name = models.CharField("Цвет", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'


class Material(models.Model):
    name = models.CharField("Материал", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'


class Glass(models.Model):
    name = models.CharField("Стекло", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стекло'
        verbose_name_plural = 'Стекло'


class Waterproof(models.Model):
    name = models.CharField("Водонепраницаемость", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Водонепраницаемость'
        verbose_name_plural = 'Водонепраницаемость'


class Numbers(models.Model):
    name = models.CharField("Цифры", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цифры'
        verbose_name_plural = 'Цифры'


class ZipType(models.Model):
    name = models.CharField("Тип застёжки", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип застёжки'
        verbose_name_plural = 'Тип застёжки'


"""

class BezelMaterial(models.Model):
    name = models.CharField("Материал безеля", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал безеля'
        verbose_name_plural = 'Материал безеля'


class BracerMaterial(models.Model):
    name = models.CharField("Материал браслета", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал браслета'
        verbose_name_plural = 'Материал браслета'


class ZipMaterial(models.Model):
    name = models.CharField("Материал застёжки", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал застёжки'
        verbose_name_plural = 'Материал застёжки'
"""


class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField('Название часов', max_length=150)
    id_number = models.CharField('Идентификационный номер', max_length=30, null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2, null=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)
    year = models.IntegerField("Год выпуска", null=True, blank=True)
    diameter1 = models.IntegerField('Диаметр1 мм', null=True, blank=True)
    diameter2 = models.IntegerField('Диаметр2 мм', null=True, blank=True)
    sex = models.ForeignKey(
        Sex,
        on_delete=models.CASCADE,
        verbose_name='Пол',
        null=True,
        blank=True,
    )
    watch_type = models.ForeignKey(
        WatchType,
        on_delete=models.CASCADE,
        verbose_name='Тип часов',
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Бренд',
        null=True,
        blank=True,
    )
    condition = models.ForeignKey(
        Condition,
        on_delete=models.CASCADE,
        verbose_name='Состояние часов',
        null=True,
        blank=True,
    )
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        verbose_name='Комплектация',
        null=True,
        blank=True,
    )
    meh_type = models.ForeignKey(
        MehType,
        on_delete=models.CASCADE,
        verbose_name='Тип механизма',
        null=True,
        blank=True,
    )
    # Калибр
    caliber = models.CharField('Калибр/Механизм', max_length=30, null=True, blank=True)
    base_caliber = models.CharField('Базовый калибр', max_length=30, null=True, blank=True)
    cruising_range = models.CharField('Запас хода', max_length=30, null=True, blank=True)
    stones = models.CharField('Количество камней', max_length=30, null=True, blank=True)
    vibration = models.CharField('Частота вибрации баланса', max_length=30, null=True, blank=True)
    jenev_mark = models.BooleanField('Женевское клеймо', null=True, blank=True, default=False)
    chronometer = models.BooleanField('Хронометр', null=True, blank=True, default=False)
    master_chronometer = models.BooleanField('Мастер хронометр', null=True, blank=True, default=False)

    # photo = models.ImageField("Фото",
    # upload_to="img/admin_watch",
    # height_field=None,
    # width_field=None,
    # max_length=120,
    # null=True,
    # blank=True
    # )

    # Корпус
    corpus_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Материал корпуса',
        related_name='corpus_material',
        null=True,
        blank=True,
    )  # Material
    bezel_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Материал безеля',
        related_name='bezel_material',
        null=True,
        blank=True,
    )  # Material
    thickness = models.CharField('Толщина', max_length=30, null=True, blank=True)
    glass = models.ForeignKey(
        Glass,
        on_delete=models.CASCADE,
        verbose_name='Стекло',
        null=True,
        blank=True,
    )
    waterproof = models.ForeignKey(
        Waterproof,
        on_delete=models.CASCADE,
        verbose_name='Водонепроницаемость',
        null=True,
        blank=True,
    )
    back_cap = models.BooleanField('Прозрачная задняя крышка', null=True, blank=True, default=False)
    jewelry = models.BooleanField('Отделка драгоценными камнями', null=True, blank=True, default=False)
    spraying = models.BooleanField('PVD/DLS напыление', null=True, blank=True, default=False)

    # Циферблат и стрелки
    dial = models.ForeignKey(
        Colour,
        on_delete=models.CASCADE,
        verbose_name='Циферблат',
        related_name='dial_colour',
        null=True,
        blank=True,
    )  # Color
    numbers = models.ForeignKey(
        Numbers,
        on_delete=models.CASCADE,
        verbose_name='Цифры',
        null=True,
        blank=True,
    )
    dial1 = models.BooleanField('Гильошированный циферблат', null=True, blank=True, default=False)
    dial2 = models.BooleanField('Ручное гильоширование', null=True, blank=True, default=False)
    dial3 = models.BooleanField('Люминисцентные цифры', null=True, blank=True, default=False)

    numbers1 = models.BooleanField('Центральная секундная стрелка', null=True, blank=True, default=False)
    numbers2 = models.BooleanField('Малый секундный циферблат', null=True, blank=True, default=False)
    numbers3 = models.BooleanField('Люминисцентные стрелки', null=True, blank=True, default=False)
    numbers4 = models.BooleanField('Стрелки из оксидированной стали', null=True, blank=True, default=False)

    # Браслет

    bracer = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Материал браслета',
        related_name='bracer',
        null=True,
        blank=True,
    )  # Material
    bracer_colour = models.ForeignKey(
        Colour,
        on_delete=models.CASCADE,
        verbose_name='Цвет браслета',
        related_name='bracer_colour',
        null=True,
        blank=True,
    )  # Color
    zip_type = models.ForeignKey(
        ZipType,
        on_delete=models.CASCADE,
        verbose_name='Материал застёжки',
        null=True,
        blank=True,
    )
    zip_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name='Тип застёжки',
        related_name='zip_material',
        null=True,
        blank=True,
    )  # Material

    # Функции
    moon_faze = models.BooleanField('Индикатор фазы луны', null=True, blank=True, default=False)
    chronograf = models.BooleanField('Хронограф', null=True, blank=True, default=False)
    flyback = models.BooleanField('Flyback-функция', null=True, blank=True, default=False)
    the_striking_mechanism = models.BooleanField('Механизм боя', null=True, blank=True, default=False)
    turbion = models.BooleanField('Турбийон', null=True, blank=True, default=False)
    day_in_week = models.BooleanField('Индикатор дней недели', null=True, blank=True, default=False)
    day_in_year = models.BooleanField('Индикатор года', null=True, blank=True, default=False)
    calendar_on_4_years = models.BooleanField('Календарь на 4 года', null=True, blank=True, default=False)
    alarm_clock = models.BooleanField('Будильник', null=True, blank=True, default=False)
    calendar_of_time = models.BooleanField('Уравнение времени', null=True, blank=True, default=False)
    tahimetr = models.BooleanField('Тахиметр', null=True, blank=True, default=False)
    minute_repeater = models.BooleanField('Минутный репитор', null=True, blank=True, default=False)
    split_chronograf = models.BooleanField('Сплит-хронограф', null=True, blank=True, default=False)
    panoramic_date = models.BooleanField('Панорамная дата', null=True, blank=True, default=False)
    repeater = models.BooleanField('Репитер', null=True, blank=True, default=False)
    date = models.BooleanField('Дата', null=True, blank=True, default=False)
    month_indicator = models.BooleanField('Индикатор месяца', null=True, blank=True, default=False)
    year_calendar = models.BooleanField('Годовой календарь', null=True, blank=True, default=False)
    eternal_calendar = models.BooleanField('Вечный календарь', null=True, blank=True, default=False)
    gmt = models.BooleanField('GMT/две часовые зоны', null=True, blank=True, default=False)
    jump_hour = models.BooleanField('Прыгающий час', null=True, blank=True, default=False)

    def get_image_filename(instance, filename):
        name = instance.post.name
        slug = slugify(name)
        return "post_images/%s-%s" % (slug, filename)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class Images(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='media',
        verbose_name='Image',
        null=True,
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
