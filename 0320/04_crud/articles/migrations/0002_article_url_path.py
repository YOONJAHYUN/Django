# Generated by Django 3.2.18 on 2023-03-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url_path',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]