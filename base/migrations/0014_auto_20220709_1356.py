# Generated by Django 3.2.11 on 2022-07-09 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_subcategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothingandbeauty',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='electronic',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='category',
            new_name='subcategory',
        ),
    ]
