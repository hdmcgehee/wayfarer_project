# Generated by Django 3.1 on 2020-08-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200805_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default='no country selected', max_length=50),
            preserve_default=False,
        ),
    ]
