# Generated by Django 5.2.3 on 2025-06-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sales', models.PositiveIntegerField(default=0)),
                ('best_seller', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
