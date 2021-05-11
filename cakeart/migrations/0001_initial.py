# Generated by Django 2.0 on 2020-03-19 11:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnty', models.IntegerField(default=1)),
                ('rowtotal', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('category_img', models.ImageField(default='abc.jpg', upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decoration_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_abt', models.CharField(default='', max_length=20, null=True)),
                ('feedback_text', models.CharField(max_length=500)),
                ('feedback_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('prc', models.FloatField(default=0.0)),
                ('cnm', models.CharField(default='', max_length=50)),
                ('dt', models.DateField(blank=True, default=datetime.date.today, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillingAddress', models.CharField(max_length=130)),
                ('order_dt', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('TotalPrice', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=30)),
                ('package_price', models.IntegerField(blank=True, null=True)),
                ('package_validity', models.CharField(max_length=30)),
                ('package_discount', models.IntegerField(blank=True, null=True)),
                ('package_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(default='', max_length=50)),
                ('omid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.OrderMaster')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_type', models.CharField(max_length=20)),
                ('product_desc', models.CharField(max_length=500)),
                ('product_image', models.ImageField(default='', upload_to='image/')),
                ('qnty', models.IntegerField(blank=True, default=5, null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Category')),
                ('decoration_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Decoration')),
                ('flavor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cakeart.Flavour')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_type', models.CharField(max_length=20)),
                ('product_desc', models.CharField(max_length=500)),
                ('product_image', models.ImageField(default='', upload_to='image/')),
                ('qty', models.IntegerField(default=5)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Category')),
                ('decoration_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Decoration')),
                ('flavor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cakeart.Flavour')),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(default='GENERAL', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('pinc', models.IntegerField()),
                ('License', models.FileField(default='', upload_to='file/')),
                ('shopnm', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('email', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=10)),
                ('otp', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='utid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User_type'),
        ),
        migrations.AddField(
            model_name='products',
            name='shape_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Shape'),
        ),
        migrations.AddField(
            model_name='products',
            name='theme_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Theme'),
        ),
        migrations.AddField(
            model_name='products',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='shape_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Shape'),
        ),
        migrations.AddField(
            model_name='product',
            name='theme_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Theme'),
        ),
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
        migrations.AddField(
            model_name='payment',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
        migrations.AddField(
            model_name='ordermaster',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
        migrations.AddField(
            model_name='orderdetailing',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.OrderMaster'),
        ),
        migrations.AddField(
            model_name='orderdetailing',
            name='prodid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Product'),
        ),
        migrations.AddField(
            model_name='orderdetailing',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='to_vb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='prodid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeart.User'),
        ),
    ]