# Generated by Django 2.2.8 on 2019-12-07 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='configuration',
            unique_together={('application', 'environment')},
        ),
    ]
