# Generated by Django 4.0.3 on 2022-06-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('cin', models.CharField(blank=True, max_length=30, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('lodging', models.CharField(blank=True, choices=[('With Garden', 'with garden'), ('Without Garden', 'without garden')], max_length=15, null=True)),
                ('fammilial_status', models.CharField(blank=True, choices=[('Married', 'married'), ('Divorced', 'divorced'), ('Separated', 'separated'), ('Single', 'single'), ('Widow(er)', 'widow(er)')], max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
