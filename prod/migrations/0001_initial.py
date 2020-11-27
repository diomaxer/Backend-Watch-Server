# Generated by Django 3.1.3 on 2020-11-27 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Бренд часов')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвет',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Состояние часов')),
            ],
            options={
                'verbose_name': 'Состояние часов',
                'verbose_name_plural': 'Состояние часов',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Комплектация')),
            ],
            options={
                'verbose_name': 'Комплектация',
                'verbose_name_plural': 'Комплектация',
            },
        ),
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Стекло')),
            ],
            options={
                'verbose_name': 'Стекло',
                'verbose_name_plural': 'Стекло',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материал',
            },
        ),
        migrations.CreateModel(
            name='MehType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип механизма')),
            ],
            options={
                'verbose_name': 'Тип механизма',
                'verbose_name_plural': 'Тип механизма',
            },
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Цифры')),
            ],
            options={
                'verbose_name': 'Цифры',
                'verbose_name_plural': 'Цифры',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
            },
        ),
        migrations.CreateModel(
            name='WatchType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип часов')),
            ],
            options={
                'verbose_name': 'Тип часов',
                'verbose_name_plural': 'Типы часов',
            },
        ),
        migrations.CreateModel(
            name='Waterproof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Водонепраницаемость')),
            ],
            options={
                'verbose_name': 'Водонепраницаемость',
                'verbose_name_plural': 'Водонепраницаемость',
            },
        ),
        migrations.CreateModel(
            name='ZipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип застёжки')),
            ],
            options={
                'verbose_name': 'Тип застёжки',
                'verbose_name_plural': 'Тип застёжки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название часов')),
                ('id_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Идентификационный номер')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Цена')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('diameter1', models.IntegerField(blank=True, null=True, verbose_name='Диаметр1 мм')),
                ('diameter2', models.IntegerField(blank=True, null=True, verbose_name='Диаметр2 мм')),
                ('caliber', models.CharField(blank=True, max_length=30, null=True, verbose_name='Калибр/Механизм')),
                ('base_caliber', models.CharField(blank=True, max_length=30, null=True, verbose_name='Базовый калибр')),
                ('cruising_range', models.CharField(blank=True, max_length=30, null=True, verbose_name='Запас хода')),
                ('stones', models.CharField(blank=True, max_length=30, null=True, verbose_name='Количество камней')),
                ('vibration', models.CharField(blank=True, max_length=30, null=True, verbose_name='Частота вибрации баланса')),
                ('jenev_mark', models.BooleanField(blank=True, default=False, null=True, verbose_name='Женевское клеймо')),
                ('chronometer', models.BooleanField(blank=True, default=False, null=True, verbose_name='Хронометр')),
                ('master_chronometer', models.BooleanField(blank=True, default=False, null=True, verbose_name='Мастер хронометр')),
                ('thickness', models.CharField(blank=True, max_length=30, null=True, verbose_name='Толщина')),
                ('back_cap', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прозрачная задняя крышка')),
                ('jewelry', models.BooleanField(blank=True, default=False, null=True, verbose_name='Отделка драгоценными камнями')),
                ('spraying', models.BooleanField(blank=True, default=False, null=True, verbose_name='PVD/DLS напыление')),
                ('dial1', models.BooleanField(blank=True, default=False, null=True, verbose_name='Гильошированный циферблат')),
                ('dial2', models.BooleanField(blank=True, default=False, null=True, verbose_name='Ручное гильоширование')),
                ('dial3', models.BooleanField(blank=True, default=False, null=True, verbose_name='Люминисцентные цифры')),
                ('numbers1', models.BooleanField(blank=True, default=False, null=True, verbose_name='Центральная секундная стрелка')),
                ('numbers2', models.BooleanField(blank=True, default=False, null=True, verbose_name='Малый секундный циферблат')),
                ('numbers3', models.BooleanField(blank=True, default=False, null=True, verbose_name='Люминисцентные стрелки')),
                ('numbers4', models.BooleanField(blank=True, default=False, null=True, verbose_name='Стрелки из оксидированной стали')),
                ('moon_faze', models.BooleanField(blank=True, default=False, null=True, verbose_name='Индикатор фазы луны')),
                ('chronograf', models.BooleanField(blank=True, default=False, null=True, verbose_name='Хронограф')),
                ('flyback', models.BooleanField(blank=True, default=False, null=True, verbose_name='Flyback-функция')),
                ('the_striking_mechanism', models.BooleanField(blank=True, default=False, null=True, verbose_name='Механизм боя')),
                ('turbion', models.BooleanField(blank=True, default=False, null=True, verbose_name='Турбийон')),
                ('day_in_week', models.BooleanField(blank=True, default=False, null=True, verbose_name='Индикатор дней недели')),
                ('day_in_year', models.BooleanField(blank=True, default=False, null=True, verbose_name='Индикатор года')),
                ('calendar_on_4_years', models.BooleanField(blank=True, default=False, null=True, verbose_name='Календарь на 4 года')),
                ('alarm_clock', models.BooleanField(blank=True, default=False, null=True, verbose_name='Будильник')),
                ('calendar_of_time', models.BooleanField(blank=True, default=False, null=True, verbose_name='Уравнение времени')),
                ('tahimetr', models.BooleanField(blank=True, default=False, null=True, verbose_name='Тахиметр')),
                ('minute_repeater', models.BooleanField(blank=True, default=False, null=True, verbose_name='Минутный репитор')),
                ('split_chronograf', models.BooleanField(blank=True, default=False, null=True, verbose_name='Сплит-хронограф')),
                ('panoramic_date', models.BooleanField(blank=True, default=False, null=True, verbose_name='Панорамная дата')),
                ('repeater', models.BooleanField(blank=True, default=False, null=True, verbose_name='Репитер')),
                ('date', models.BooleanField(blank=True, default=False, null=True, verbose_name='Дата')),
                ('month_indicator', models.BooleanField(blank=True, default=False, null=True, verbose_name='Индикатор месяца')),
                ('year_calendar', models.BooleanField(blank=True, default=False, null=True, verbose_name='Годовой календарь')),
                ('eternal_calendar', models.BooleanField(blank=True, default=False, null=True, verbose_name='Вечный календарь')),
                ('gmt', models.BooleanField(blank=True, default=False, null=True, verbose_name='GMT/две часовые зоны')),
                ('jump_hour', models.BooleanField(blank=True, default=False, null=True, verbose_name='Прыгающий час')),
                ('bezel_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bezel_material', to='prod.material', verbose_name='Материал безеля')),
                ('bracer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracer', to='prod.material', verbose_name='Материал браслета')),
                ('bracer_colour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracer_colour', to='prod.colour', verbose_name='Цвет браслета')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.brand', verbose_name='Бренд')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.condition', verbose_name='Состояние часов')),
                ('corpus_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corpus_material', to='prod.material', verbose_name='Материал корпуса')),
                ('dial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dial_colour', to='prod.colour', verbose_name='Циферблат')),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.equipment', verbose_name='Комплектация')),
                ('glass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.glass', verbose_name='Стекло')),
                ('meh_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.mehtype', verbose_name='Тип механизма')),
                ('numbers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.numbers', verbose_name='Цифры')),
                ('sex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.sex', verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Часы',
                'verbose_name_plural': 'Часы',
            },
        ),
    ]
