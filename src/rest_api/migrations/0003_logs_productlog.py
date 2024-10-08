# Generated by Django 3.0.6 on 2020-09-27 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0002_auto_20200922_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_log_pk', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('purchase', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('enable_product', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('all_log_id', models.IntegerField(blank=True, null=True)),
                ('has_variant', models.BooleanField(default=False)),
                ('backup_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_pk', models.IntegerField()),
                ('operation', models.CharField(blank=True, max_length=255, null=True)),
                ('detail', models.CharField(blank=True, max_length=255, null=True)),
                ('model_id', models.IntegerField(blank=True, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('backup_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
