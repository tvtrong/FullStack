# Generated by Django 3.0.7 on 2020-06-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
    ]