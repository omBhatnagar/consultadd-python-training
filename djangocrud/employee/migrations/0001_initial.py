# Generated by Django 4.1.5 on 2023-02-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='EMP_ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
