# Generated by Django 2.1.2 on 2018-11-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crane', '0020_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
    ]
