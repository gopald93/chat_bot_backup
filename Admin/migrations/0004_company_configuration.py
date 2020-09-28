# Generated by Django 3.1 on 2020-08-20 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Admin', '0003_welcome_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Configuration',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('company_urls', models.URLField(blank=True)),
                ('company_domain_name', models.CharField(blank=True, max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
