# Generated by Django 2.2.4 on 2019-08-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0005_auto_20190807_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, default='myaudio.mp3', upload_to=''),
        ),
    ]