# Generated by Django 3.0.8 on 2020-07-09 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='category',
        ),
    ]
