# Generated by Django 5.0.4 on 2024-05-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('producttype', models.CharField(max_length=20)),
            ],
        ),
    ]
