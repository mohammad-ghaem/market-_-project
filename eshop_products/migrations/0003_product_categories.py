# Generated by Django 3.0.6 on 2020-07-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0002_auto_20200701_1043'),
        ('eshop_products', '0002_auto_20200624_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='eshop_products_category.ProductCategory', verbose_name='دسته بندی ها'),
        ),
    ]
