# Generated by Django 3.0.6 on 2020-08-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0002_sitesetting_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='copy_right',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='متن کپی رایت'),
        ),
    ]
