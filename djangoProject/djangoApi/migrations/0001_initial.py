# Generated by Django 3.1.2 on 2020-10-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('sal', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]