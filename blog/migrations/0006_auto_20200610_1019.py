# Generated by Django 2.2.13 on 2020-06-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_miscellaneous_poem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellaneous',
            name='category',
            field=models.CharField(default='', max_length=300),
        ),
    ]
