# Generated by Django 3.1 on 2021-09-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_residencedetails_residenceimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('eMail', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('photoUrl', models.CharField(max_length=200)),
            ],
        ),
    ]
