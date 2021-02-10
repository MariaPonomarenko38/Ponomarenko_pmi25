# Generated by Django 3.1.3 on 2020-11-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinemeeting',
            name='owner_first_name',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Owner First Name'),
        ),
        migrations.AddField(
            model_name='onlinemeeting',
            name='owner_last_name',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Owner Last Name'),
        ),
        migrations.AddField(
            model_name='onlinemeeting',
            name='participant_first_name',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Participant First Name'),
        ),
        migrations.AddField(
            model_name='onlinemeeting',
            name='participant_last_name',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Participant Last Name'),
        ),
    ]