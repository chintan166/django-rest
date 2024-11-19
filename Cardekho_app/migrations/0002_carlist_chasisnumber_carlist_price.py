# Generated by Django 4.2 on 2024-11-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cardekho_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chasisnumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]