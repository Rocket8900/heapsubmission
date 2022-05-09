# Generated by Django 3.2.4 on 2022-04-26 10:58

from django.db import migrations, models
import food.utils


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_shop_options'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='shop',
            name='user_Referrence_Number',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='Referrence_Number',
        ),
        migrations.AddField(
            model_name='shop',
            name='referrence_Number',
            field=models.CharField(blank=True, default=food.utils.create_new_ref_number, max_length=10, unique=True),
        ),
        migrations.AddConstraint(
            model_name='shop',
            constraint=models.UniqueConstraint(fields=('user', 'referrence_Number'), name='user_Referrence_Number'),
        ),
    ]