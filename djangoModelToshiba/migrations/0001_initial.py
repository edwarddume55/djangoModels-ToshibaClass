# Generated by Django 4.2.6 on 2023-11-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toshiba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
