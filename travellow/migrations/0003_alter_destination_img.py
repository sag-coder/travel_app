# Generated by Django 3.2.3 on 2021-05-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellow', '0002_auto_20210525_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(height_field=501, max_length=115, upload_to='pix', width_field=690),
        ),
    ]
