# Generated by Django 4.1.1 on 2022-10-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_model_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_model',
            name='pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media/'),
        ),
    ]
