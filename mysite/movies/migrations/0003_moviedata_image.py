# Generated by Django 4.2.7 on 2023-11-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/None/No-img.jpg', upload_to='images/'),
        ),
    ]
