# Generated by Django 4.1 on 2022-08-30 17:32

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_sneakers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers',
            name='image',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='%y/%m/%d', variations={}),
        ),
    ]
