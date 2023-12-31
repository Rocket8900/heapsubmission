# Generated by Django 3.2.4 on 2022-04-20 10:08

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(default='nothing')),
                ('open_hours', models.TextField(default='unknown')),
                ('late_hours', models.BooleanField(default=False, verbose_name='Opens After 11pm')),
                ('directions', models.CharField(blank=True, max_length=100)),
                ('halal', models.BooleanField(default=False, verbose_name='Halal')),
                ('cuisine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.cuisine')),
                ('price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.price')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('type_of_food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.type_of_food')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
