# Generated by Django 4.0 on 2022-11-11 11:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
                ('desc', models.TextField(blank=True, default='')),
                ('career_prospectus', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='N/A', max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('credit', models.IntegerField()),
                ('programs', models.ManyToManyField(to='academics.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.program')),
                ('subjects', models.ManyToManyField(to='academics.Subject')),
            ],
        ),
    ]
