# Generated by Django 3.0.6 on 2020-05-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='result',
            field=models.ManyToManyField(blank=True, null=True, to='core.TypePrint'),
        ),
    ]