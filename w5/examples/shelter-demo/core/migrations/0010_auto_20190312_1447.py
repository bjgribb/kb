# Generated by Django 2.1.7 on 2019-03-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190312_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dogs',
            field=models.ManyToManyField(blank=True, related_name='events', to='core.Dog'),
        ),
    ]
