# Generated by Django 4.2.6 on 2024-06-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_salesreportnew_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='order_note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]