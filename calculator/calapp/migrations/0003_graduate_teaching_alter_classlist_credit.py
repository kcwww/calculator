# Generated by Django 4.1 on 2022-08-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0002_classlist_graduate_deepmajor'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduate',
            name='teaching',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='classlist',
            name='credit',
            field=models.IntegerField(null=True),
        ),
    ]