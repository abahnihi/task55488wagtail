# Generated by Django 3.1.3 on 2020-11-03 17:52

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_howsec_how_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='howsec',
            name='page',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='how_it_works', to='home.homepage'),
        ),
    ]
