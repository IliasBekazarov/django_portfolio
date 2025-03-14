# Generated by Django 5.1.7 on 2025-03-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0016_home_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='description_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='hire_me_link_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='name_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='home',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='home',
            name='description_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='home',
            name='name_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='home',
            name='title_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='project',
            name='description_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='project',
            name='title_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='skill',
            name='name_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='skill',
            name='percentage_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='testimony',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
    ]
