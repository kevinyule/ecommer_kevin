# Generated by Django 4.1.1 on 2022-09-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_personas'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='genero',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
