# Generated by Django 2.2 on 2020-09-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_permission_is_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='icon'),
        ),
    ]
