# Generated by Django 3.0.6 on 2020-05-17 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200516_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='result',
        ),
        migrations.AddField(
            model_name='profile',
            name='result',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.TypePrint'),
            preserve_default=False,
        ),
    ]