# Generated by Django 3.1.1 on 2020-09-16 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20200916_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iconar2ns',
            name='icon_creation_date',
        ),
    ]
