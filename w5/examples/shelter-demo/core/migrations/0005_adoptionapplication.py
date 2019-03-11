# Generated by Django 2.1.7 on 2019-03-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_dog_energy_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('current_pets', models.PositiveIntegerField(verbose_name='Number of current pets')),
                ('fenced_backyard', models.BooleanField(verbose_name='Do you have a fenced backyard?')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='core.Dog')),
            ],
        ),
    ]