from rest_framework import serializers
from .models import Images, Product, Sex, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType


class SexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sex
        fields = "__all__"


class WatchTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchType
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class MehTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MehType
        fields = "__all__"


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"


class ColourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colour
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class GlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glass
        fields = "__all__"


class WaterproofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterproof
        fields = "__all__"


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = "__all__"


class ZipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipType
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user')
    sex_name = serializers.CharField(source='sex')
    watch_type_name = serializers.CharField(source='watch_type')
    brand_name = serializers.CharField(source='brand')
    condition_name = serializers.CharField(source='condition')
    equipment_name = serializers.CharField(source='equipment')
    meh_type_name = serializers.CharField(source='meh_type')
    corpus_material_name = serializers.CharField(source='corpus_material')
    bezel_material_name = serializers.CharField(source='bezel_material')
    glass_name = serializers.CharField(source='glass')
    waterproof_name = serializers.CharField(source='waterproof')
    dial_name = serializers.CharField(source='dial')
    numbers_name = serializers.CharField(source='numbers')
    bracer_name = serializers.CharField(source='bracer')
    bracer_colour_name = serializers.CharField(source='bracer_colour')
    zip_type_name = serializers.CharField(source='zip_type')
    zip_material_name = serializers.CharField(source='zip_material')


    class Meta:
        model = Product
        fields = [
            'user_username',
            'name',
            'id_number',
            'description',
            'price',
            'year',
            'diameter1',
            'diameter2',
            'sex_name',
            'watch_type_name',
            'brand_name',
            'condition_name',
            'equipment_name',
            'meh_type_name',

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

            'corpus_material_name',
            'bezel_material_name',
            'thickness',
            'glass_name',
            'waterproof_name',
            'back_cap',

            # Циферблат и стрелки

            'dial_name',
            'numbers_name',
            'dial1',
            'dial2',
            'dial3',
            'numbers1',
            'numbers2',
            'numbers3',
            'numbers4',

            # Браслет

            'bracer_name',
            'bracer_colour_name',
            'zip_type_name',
            'zip_material_name',

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


class ProductSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        # depth=1


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'