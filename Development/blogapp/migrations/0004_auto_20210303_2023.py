# Generated by Django 2.0.3 on 2021-03-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20201010_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='mobile',
            field=models.CharField(blank=True, max_length=18),
        ),
    ]
