# Generated by Django 2.2 on 2020-10-19 07:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveSmallIntegerField(default=0)),
                ('desc', models.TextField(default='', max_length=50)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terjual', to='products.Prod')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesuai', to='sales.Sale')),
            ],
        ),
    ]
