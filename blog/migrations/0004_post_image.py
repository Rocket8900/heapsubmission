# Generated by Django 3.2.4 on 2022-05-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
