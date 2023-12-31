# Generated by Django 4.2.5 on 2023-09-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("image", "0002_remove_expiringlink_expiry_time_and_more"),
        ("accounts", "0002_useraccount_account_tier"),
    ]

    operations = [
        migrations.AddField(
            model_name="accounttier",
            name="get_original_file",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="accounttier",
            name="thumbnail_sizes",
            field=models.ManyToManyField(blank=True, to="images.thumbnailsize"),
        ),
        migrations.AlterField(
            model_name="useraccount",
            name="account_tier",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="users", to="accounts.accounttier"
            ),
        ),
    ]