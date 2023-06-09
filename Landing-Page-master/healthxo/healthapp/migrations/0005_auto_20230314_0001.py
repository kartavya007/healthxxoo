# Generated by Django 3.2.16 on 2023-03-13 18:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0004_diet_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='start',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
