# Generated by Django 5.2.4 on 2025-07-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('shop', '0009_alter_color_title_alter_detail_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='category',
            field=models.ManyToManyField(to='home.category'),
        ),
    ]
