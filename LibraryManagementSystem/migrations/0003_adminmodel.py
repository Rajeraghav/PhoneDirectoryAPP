# Generated by Django 3.2.15 on 2022-09-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0002_auto_20220910_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookId', models.CharField(default='', max_length=70)),
                ('BookName', models.CharField(default='', max_length=70)),
                ('AuthorName', models.CharField(default='', max_length=70)),
                ('BookPrice', models.CharField(default='', max_length=70)),
            ],
        ),
    ]