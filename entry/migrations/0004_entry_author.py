# Generated by Django 3.0 on 2020-06-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_auto_20200608_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
