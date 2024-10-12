# Generated by Django 5.1.2 on 2024-10-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransferEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.BigIntegerField()),
                ('from_address', models.CharField(max_length=42)),
                ('to_address', models.CharField(max_length=42)),
                ('transaction_hash', models.CharField(max_length=66)),
                ('block_number', models.IntegerField()),
            ],
        ),
    ]
