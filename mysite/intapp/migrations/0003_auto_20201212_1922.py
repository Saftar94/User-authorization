# Generated by Django 3.0.7 on 2020-12-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intapp', '0002_auto_20201205_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='password',
            field=models.CharField(max_length=250, verbose_name='password'),
        ),
    ]
