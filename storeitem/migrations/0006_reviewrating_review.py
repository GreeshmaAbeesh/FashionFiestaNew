# Generated by Django 4.2.6 on 2024-03-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeitem', '0005_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='review',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
