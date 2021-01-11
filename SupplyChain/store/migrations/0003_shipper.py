# Generated by Django 3.1.4 on 2021-01-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210109_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=15)),
                ('To', models.CharField(max_length=15)),
                ('Days', models.IntegerField(max_length=1)),
            ],
        ),
    ]