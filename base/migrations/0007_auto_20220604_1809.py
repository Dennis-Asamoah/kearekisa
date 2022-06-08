# Generated by Django 3.2.11 on 2022-06-04 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220604_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingandbeauty',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
        migrations.AlterField(
            model_name='electronic',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
    ]