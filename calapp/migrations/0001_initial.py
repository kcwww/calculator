# Generated by Django 4.1.3 on 2022-11-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50, null=True)),
                ('classname', models.CharField(max_length=50, null=True)),
                ('credit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=50, null=True)),
                ('ad_year', models.CharField(max_length=50, null=True)),
                ('basic', models.IntegerField(null=True)),
                ('balance', models.IntegerField(null=True)),
                ('college', models.IntegerField(null=True)),
                ('free', models.IntegerField(null=True)),
                ('needmajor', models.IntegerField(null=True)),
                ('choicemajor', models.IntegerField(null=True)),
                ('deepmajor', models.IntegerField(null=True)),
                ('special', models.IntegerField(null=True)),
                ('teaching', models.IntegerField(null=True)),
                ('sum', models.IntegerField(null=True)),
            ],
        ),
    ]
