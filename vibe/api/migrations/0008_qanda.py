# Generated by Django 3.1 on 2021-09-08 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(max_length=400)),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.residencedetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
