# Generated by Django 2.2.7 on 2020-10-01 07:33

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=12)),
                ('real_name', models.CharField(max_length=60)),
                ('tz', timezone_field.fields.TimeZoneField(default='America/Los_Angeles')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('member', models.ManyToManyField(to='api.Member')),
            ],
        ),
    ]
