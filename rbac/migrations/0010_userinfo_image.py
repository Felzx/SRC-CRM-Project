# Generated by Django 2.2 on 2020-10-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0009_auto_20200921_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]