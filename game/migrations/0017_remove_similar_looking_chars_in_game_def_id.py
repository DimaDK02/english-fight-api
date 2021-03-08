# Generated by Django 3.1.3 on 2021-03-08 16:34

import hashid_field.field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_gamedefinition_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedefinition',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghjkmnpqrstuvwxyz123456789', min_length=7, primary_key=True, serialize=False),
        ),
    ]
