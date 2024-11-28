# Generated by Django 4.2.3 on 2024-11-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=16)),
                ('category', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('availability', models.BooleanField()),
            ],
        ),
    ]
