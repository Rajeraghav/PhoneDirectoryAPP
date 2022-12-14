# Generated by Django 3.2.15 on 2022-09-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0006_auto_20220925_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='addUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(blank=True, null=True)),
                ('user', models.BooleanField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('mobileNumber', models.IntegerField(blank=True, null=True)),
                ('password1', models.CharField(blank=True, max_length=100, null=True)),
                ('password2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cartBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterId', models.IntegerField(blank=True, null=True)),
                ('enterName', models.CharField(blank=True, max_length=100, null=True)),
                ('enterAuthorName', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
