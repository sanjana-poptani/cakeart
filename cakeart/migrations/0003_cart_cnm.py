# Generated by Django 2.0 on 2020-03-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeart', '0002_remove_product_qnty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cnm',
            field=models.CharField(default='', max_length=100),
        ),
    ]
