from django import forms

from .models import Product, Images

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'id_number',
            'description',
            'price',
            'year',
            'diameter1',
            'diameter2',
            'sex',
            'watch_type',
            'brand',
            'condition',
            'equipment',
            'meh_type',

            # Калибр

            'caliber',
            'base_caliber',
            'cruising_range',
            'stones',
            'vibration',
            'jenev_mark',
            'chronometer',
            'master_chronometer',
            #'photo',

            # Корпус

            'corpus_material',
            'bezel_material',
            'thickness',
            'glass',
            'waterproof',
            'back_cap',

            # Циферблат и стрелки

            'dial',
            'numbers',
            'dial1',
            'dial2',
            'dial3',
            'numbers1',
            'numbers2',
            'numbers3',
            'numbers4',

            # Браслет

            'bracer',
            'bracer_colour',
            'zip_type',
            'zip_material',

            # Функции

            'moon_faze',
            'chronograf',
            'flyback',
            'the_striking_mechanism',
            'turbion',
            'day_in_week',
            'day_in_year',
            'calendar_on_4_years',
            'alarm_clock',
            'calendar_of_time',
            'tahimetr',
            'minute_repeater',
            'split_chronograf',
            'panoramic_date',
            'repeater',
            'date',
            'month_indicator',
            'year_calendar',
            'eternal_calendar',
            'gmt',
            'jump_hour',
        ]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )