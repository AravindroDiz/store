# Generated by Django 4.2.5 on 2023-11-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.IntegerField(default=False),
        ),
    ]
