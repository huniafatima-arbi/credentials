# Generated by Django 3.2.15 on 2022-09-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0020_auto_20220912_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergrade',
            name='lms_last_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]