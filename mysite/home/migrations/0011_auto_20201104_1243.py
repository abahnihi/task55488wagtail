# Generated by Django 3.1.3 on 2020-11-04 12:43

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
        ('home', '0010_auto_20201104_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_info',
            field=modelcluster.fields.ParentalManyToManyField(to='mysite.ContactInfo'),
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='partner',
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner',
            field=modelcluster.fields.ParentalManyToManyField(to='mysite.Partner'),
        ),
    ]
