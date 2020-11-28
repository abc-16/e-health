# Generated by Django 3.1.3 on 2020-11-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=15)),
                ('bloodGroup', models.CharField(max_length=4)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
