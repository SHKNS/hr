# Generated by Django 3.1.7 on 2021-03-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
