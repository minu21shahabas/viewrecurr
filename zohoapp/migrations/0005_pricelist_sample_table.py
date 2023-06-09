# Generated by Django 3.2.18 on 2023-05-17 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0004_auto_20230517_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=255)),
                ('tax', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('mark', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
                ('roundoff', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('status', models.TextField(default='active')),
                ('itemtable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sample_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('cust_rate', models.IntegerField()),
                ('pl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.pricelist')),
            ],
        ),
    ]
