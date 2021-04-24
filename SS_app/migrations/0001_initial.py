# Generated by Django 3.0.7 on 2021-04-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adminid', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('mobile', models.BigIntegerField(blank=True, default=0, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
