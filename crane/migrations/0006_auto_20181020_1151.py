# Generated by Django 2.1.2 on 2018-10-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crane', '0005_carousel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ('position',)},
        ),
        migrations.AddField(
            model_name='carousel',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
