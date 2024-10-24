# Generated by Django 5.1.1 on 2024-10-24 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_department_user_departmentname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quali', models.CharField(choices=[(1, 'M.Tech'), (2, 'B.Tech'), (3, 'BCA'), (4, 'BBA')], max_length=50)),
                ('exp', models.IntegerField()),
                ('skill', models.CharField(max_length=50)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
