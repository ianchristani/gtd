# Generated by Django 4.1.1 on 2022-10-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_model',
            name='pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
