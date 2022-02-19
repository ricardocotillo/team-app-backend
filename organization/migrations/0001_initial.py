# Generated by Django 4.0.2 on 2022-02-19 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=5)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.sport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at')),
                ('nickname', models.CharField(max_length=16)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='organization.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]