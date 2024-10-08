# Generated by Django 3.0.6 on 2020-10-01 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0006_backuplogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_pk', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('include_in_drawer', models.BooleanField(default=False)),
                ('backup_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
