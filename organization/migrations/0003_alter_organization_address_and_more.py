# Generated by Django 4.0.2 on 2022-02-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_member_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='zip_code',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
