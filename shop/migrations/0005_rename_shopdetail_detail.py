# Generated by Django 5.2.4 on 2025-07-13 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shopdetail_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShopDetail',
            new_name='Detail',
        ),
    ]
