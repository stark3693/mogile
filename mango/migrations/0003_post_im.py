# Generated by Django 4.0.5 on 2022-07-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango', '0002_post_image2_post_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='im',
            field=models.ImageField(default='', upload_to='cadd/images'),
        ),
    ]
