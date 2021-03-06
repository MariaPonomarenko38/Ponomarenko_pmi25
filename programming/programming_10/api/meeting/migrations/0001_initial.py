# Generated by Django 3.1.4 on 2020-12-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True, max_length=10, verbose_name='date')),
                ('start_time', models.TimeField(db_index=True, max_length=5, verbose_name='start_time')),
                ('end_time', models.TimeField(db_index=True, max_length=5, verbose_name='end_time')),
                ('meeting_url', models.URLField(db_index=True, verbose_name='meeting_url')),
                ('owner_first_name', models.CharField(db_index=True, default='', max_length=50, verbose_name='Owner First Name')),
                ('owner_last_name', models.CharField(db_index=True, default='', max_length=50, verbose_name='Owner Last Name')),
                ('max_count', models.IntegerField(db_index=True, default=10, verbose_name='Max quantity of participants')),
            ],
        ),
    ]
