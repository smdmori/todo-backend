# Generated by Django 3.0.8 on 2020-07-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20200709_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
