# Generated by Django 3.2.11 on 2022-06-26 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20220626_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subregion',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region', to='base.region'),
        ),
    ]