# Generated by Django 3.1 on 2020-09-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_auto_20200902_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='google_dialog_flow_integration',
            name='Service_account_private_key_file',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]
