# Generated by Django 2.2.14 on 2020-07-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200727_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='slug',
            field=models.SlugField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
