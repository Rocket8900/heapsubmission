# Generated by Django 3.2.4 on 2022-02-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_shop_directions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='website',
        ),
        migrations.AlterField(
            model_name='shop',
            name='late_hours',
            field=models.BooleanField(default=False, verbose_name='Opens After 11pm'),
        ),
    ]
