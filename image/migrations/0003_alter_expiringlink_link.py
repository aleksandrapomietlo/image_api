# Generated by Django 4.2.5 on 2023-09-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_remove_expiringlink_expiry_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiringlink',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]