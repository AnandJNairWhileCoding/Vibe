# Generated by Django 3.1 on 2021-09-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210909_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residenceId', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('report', models.CharField(max_length=25)),
            ],
        ),
    ]
