# Generated by Django 3.2.9 on 2021-12-03 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=50)),
                ('vehicle_id', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('no', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('sex', models.BooleanField(default=True)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.vehicle')),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
