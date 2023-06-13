# Generated by Django 3.2.4 on 2022-06-01 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20220512_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='type_of_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.type_of_item'),
        ),
    ]