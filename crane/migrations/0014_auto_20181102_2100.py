# Generated by Django 2.1.2 on 2018-11-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crane', '0013_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
